#!/usr/bin/env python3
"""Reorder lecture 6: move two-part tariffs before oligopoly content."""

file_path = "/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/slides/lecture_06/lecture_06.tex"

with open(file_path, 'r') as f:
    lines = f.readlines()

# Find section boundaries
preamble_end = None
oligopoly_start = None
oligopoly_end = None
twopart_start = None
twopart_end = None
keypoints_start = None

for i, line in enumerate(lines):
    if line.strip() == r'\begin{document}':
        preamble_end = i
    elif '% COURNOT AND BERTRAND' in line or '% TWO-PART TARIFFS AND OLIGOPOLY' in line:
        continue  # Skip old section markers
    elif line.strip() == r'\begin{frame}{Non-linear pricing}':
        if twopart_start is None:  # First occurrence after move
            oligopoly_start = i - 3 if i > 3 else 0  # Back up to catch section header
    elif line.strip() == r'\begin{frame}{From ECN 532: Oligopoly models}':
        if oligopoly_start is None:
            oligopoly_start = i - 3 if i > 3 else 0
    elif '% TWO-PART TARIFFS' in line and 'OLIGOPOLY' not in line:
        twopart_start = i
    elif '% KEY POINTS' in line:
        keypoints_start = i
        twopart_end = i
        oligopoly_end = i
        break

# Find the first Plan slide after document begins
first_plan = None
for i in range(preamble_end, min(preamble_end + 20, len(lines))):
    if r'\begin{frame}{Plan}' in lines[i]:
        first_plan = i
        break

# Extract sections
preamble = lines[:first_plan]
plan_and_space = lines[first_plan:oligopoly_start]
oligopoly_section = lines[oligopoly_start:twopart_start]
twopart_section = lines[twopart_start:keypoints_start]
ending = lines[keypoints_start:]

# Update Plan slides in sections to reflect new order
def update_plan_slide(section_lines, bold_item):
    """Update plan slides to have correct ordering and bold the specified item."""
    new_order = [
        r"    \item Two-part tariffs: structure and intuition",
        r"    \item Optimal two-part tariff (homogeneous consumers)",
        r"    \item Heterogeneous consumers (brief)",
        r"    \item Cournot competition (refresher)",
        r"    \item Bertrand competition (refresher)",
        r"    \item Escaping the Bertrand paradox",
    ]

    result = []
    i = 0
    while i < len(section_lines):
        line = section_lines[i]
        if r'\begin{frame}{Plan}' in line:
            # Found a plan slide - replace it
            result.append(line)  # \begin{frame}{Plan}
            i += 1
            result.append(section_lines[i])  # \begin{wideenumerate}
            i += 1

            # Skip old items until we hit \end{wideenumerate}
            while i < len(section_lines) and r'\end{wideenumerate}' not in section_lines[i]:
                i += 1

            # Insert new items
            for item in new_order:
                if bold_item in item:
                    result.append(item.replace(r"\item", r"\item \textbf{") + "}" + "\n")
                else:
                    result.append(item + "\n")

            # Add the \end{wideenumerate}
            if i < len(section_lines):
                result.append(section_lines[i])
                i += 1
        else:
            result.append(line)
            i += 1

    return result

# Update plan slides
twopart_updated = update_plan_slide(twopart_section, "Two-part tariffs")
oligopoly_updated = update_plan_slide(oligopoly_section, "Cournot competition")

# Reassemble file with new order
new_content = (
    preamble +
    plan_and_space +
    ["\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n",
     "% TWO-PART TARIFFS\n",
     "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n"] +
    twopart_updated +
    ["\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n",
     "% OLIGOPOLY REFRESHER\n",
     "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n"] +
    oligopoly_updated +
    ending
)

# Write back
with open(file_path, 'w') as f:
    f.writelines(new_content)

print("Reordered lecture_06.tex successfully")
