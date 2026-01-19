"""Take screenshots of HTML files in headless mode."""

from playwright.sync_api import sync_playwright
from pathlib import Path

figures_dir = Path(__file__).parent.parent / "slides" / "lecture_03" / "figures"

screenshots = [
    ("data_preview.html", "data_preview.png", 800, 520),
    ("results_output.html", "results_output.png", 550, 380),
    ("elasticities.html", "elasticities.png", 600, 340),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for html_file, png_file, width, height in screenshots:
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(f"file://{figures_dir / html_file}")
        page.screenshot(path=str(figures_dir / png_file))
        print(f"Saved: {png_file}")
        page.close()

    browser.close()

print("Done!")
