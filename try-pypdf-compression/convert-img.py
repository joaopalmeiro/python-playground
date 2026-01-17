from pathlib import Path

import humanize
import pymupdf

INPUT_PDF = Path("WW5000J_BETTER_SEPM_03793M-00_PT.pdf")
OUTPUT_PDF = Path("out.pdf")
IMG = Path("img")

if __name__ == "__main__":
    doc = pymupdf.open(INPUT_PDF)

    for page in doc:
        pix = page.get_pixmap(annots=False)
        pix.save(IMG / "input" / f"page-{page.number}.png")

    doc.close()

    doc = pymupdf.open(OUTPUT_PDF)

    for page in doc:
        pix = page.get_pixmap(annots=False)
        pix.save(IMG / "output" / f"page-{page.number}.png")

    doc.close()
