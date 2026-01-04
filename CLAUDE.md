*Course Details*
- **Course Code:** ECN 594
- **Title:** Advanced Topics in Competition Policy & Business Strategy
- **Instructor:** Nicholas Vreugdenhil
- **Days:** Monday & Wednesday
- **Times:** 8:00 AM - 10:30 AM
- **Dates:** January 21 - March 4, 2026
- **Location:** Tempe MCRD 250

*MS Program Schedule Notes*
- The MS program starts one week after undergraduate classes (first class is Wed, Jan 21)
- MLK Day (Mon, Jan 19) means a makeup lecture is scheduled for **Friday, January 23rd**
- 14 lectures total across 7 weeks
- No finals week in the MS program — final exam is during the last lecture (March 4)

*Objective*
- This is a master's level course in industrial organization (economics). I am the professor and when you create stuff think about it from this perspective!
- However, the students are at the advanced undergraduate level (but with potentially some average undergraduate level ones). Keep this in mind when making content.
- Claude will help with designing course architecture, slides, homework

*Course Description (for syllabus/materials)*
This is an advanced course in "Industrial Organization", which is the study of firm and consumer behavior with a particular focus on competition. The field addresses fundamental questions about when markets benefit society and where there may be scope for regulation. In addition, industrial organization economists work within businesses (particularly in tech) to design pricing and online marketplaces; while not a central focus of this course, I will occasionally mention these applications. Overall, the course will equip you with tools and concepts essential for analyzing firm strategy and for designing effective public policy.
 
*Key items (read or copy but don't change directly)*
- Previous versions of an undergraduate course and phd course are in `previous_courses/`.
- `Slides/alvins_course` contains slides for a course I didn't teach, but that they should know from last semester
- I intend to reuse *a lot* of previous content from these courses (updated to an advanced undergraduate/empirical industrial organization level). The empirical demand estimation content will draw from the PhD course. Everything else will draw from the undergraduate level.

*Textbooks and external reference material*
- `external/` contains textbooks and other reference material
- The main textbooks for this master's course are: the cabral `intro to industrial organization` textbook, and the `handbook of industrial organization vol 4 chapter 2` plus the `train, discrete choice` textbook.
- The undergraduate course ALSO uses the cabral textbook as its basis. This is useful to remember when making new content!
- The PhD demand slides mainly rely on `handbook of industrial organization vol 4 chapter 2`

*CRITICAL: How to read textbooks in external/*
- **NEVER read the original PDFs directly** (e.g., `external/cabral_solutions.pdf`, `external/train_textbook.pdf`). These are too large and will fail.
- Textbooks are split into 25-page chunks in `external/<name>_chunks/` folders
- Each chunk folder contains:
  - `markdown/` - **Search and read these FIRST**. Contains `.md` files with extracted text + `_images/` subfolders with figures
  - `pdfs/` - Original PDF chunks (25 pages each). Read these if markdown is insufficient (e.g., complex equations, tables, or layout issues)
- Workflow: Search `.md` files first for content, fall back to PDF chunks only when needed
- Available textbook chunks:
  - `cabral_solutions_chunks/` - Solutions manual (89 pages, 4 chunks)
  - `hio4_chapter2_chunks/` - Handbook of IO Vol 4 Ch 2 (96 pages, 4 chunks)
  - `peppall_textbook_chunks/` - Peppall IO textbook (725 pages, 29 chunks)
  - `train_textbook_chunks/` - Train discrete choice (388 pages, 16 chunks)
- **Textbook summaries** (read these first to locate relevant chunks):
  - `external/peppall_textbook_summary.md` - Full chapter/topic index with key equations
  - `external/hio4_chapter2_summary.md` - Demand estimation methods summary
  - `external/train_textbook_summary.md` - Discrete choice models summary
  - `external/cabral_solutions_summary.md` - Solutions manual index by chapter

*Format*
- Follow the .tex format that I use in `previous_courses/undergraduate_io` for new slides or syllabus 

*Structure*
- Structure of the course is `Masters IO dates.xlsx`.
- Each lecture has two parts. *Each* part will go for 60-75 minutes. This should be the length of time for each slide deck (20-30 slides).
- Homework will be similar to the phd_io course, but simpler in that there are not random effects. It will also be completed using statsmodels and the pyblp package in python.

*Homework Notes*
- **HW1:** Demand estimation only (Python) - due before midterm
  - Based on `previous_courses/phd_io/` homework 1, adapted for masters level
  - Key difference: uses **pyblp** package instead of custom code
  - Slides should prepare students for this homework
- **HW2:** Covers Part 2 topics (competition models). Includes a merger simulation module where students are given the demand system and compute post-merger prices/welfare effects

*Exam Notes*
- **Format:** Same as undergraduate IO course exams (see `previous_courses/undergraduate_io/exams/`)
- **Duration:** 70 minutes
- **Allowed:** Calculator + two-sided cheat sheet (letter-size paper)
- **Structure:** Mix of short answer (T/F/NEI, quick calculations, definitions) and longer problems (derivations, pricing, game theory)
- **Midterm (Feb 9):** Covers Part 1 - pricing topics tested on exam only (not HW1), demand estimation tested on both HW1 and exam
- **Final (Mar 4):** Cumulative

*Student Background (from prior MS courses)*
- From **ECN 565** (Alvin Murphy): Discrete choice econometrics (logit, probit, MLE)
- From **ECN 532** (Hector Chade): Game theory including Nash equilibrium, Cournot, Bertrand, Stackelberg, repeated games, collusion
- This means: Can do refreshers quickly in IO notation; demand estimation can focus on IO applications rather than MLE mechanics

*Course Materials*
- Syllabus: `syllabus/syllabus.tex` (compile with pdflatex)

* Environment *

This project uses **UV** for Python environment management. All Python commands must be run through UV to ensure the correct virtual environment and dependencies are used.

* Required Commands *

```bash
# Run tests
uv run pytest tests/ -v

# Run Python scripts
uv run python script.py

# Add dependencies
uv add package_name        # production
uv add --dev package_name  # development

# Sync environment after pulling changes
uv sync --all-extras
```

**Do not use bare `python` or `pytest` commands.** Always prefix with `uv run`.