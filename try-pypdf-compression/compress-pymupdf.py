from pathlib import Path

import humanize
import pymupdf

INPUT_PDF = Path("WW5000J_BETTER_SEPM_03793M-00_PT.pdf")
OUTPUT_PDF = Path("out.pdf")

if __name__ == "__main__":
    file_size = INPUT_PDF.stat().st_size
    print(humanize.naturalsize(file_size))

    doc = pymupdf.open(INPUT_PDF)

    doc.subset_fonts()

    doc.set_metadata({})
    doc.del_xml_metadata()

    doc.save(
        OUTPUT_PDF,
        garbage=4,
        deflate=True,
        deflate_images=True,
        deflate_fonts=True,
        use_objstms=1,
        clean=True,
    )

    doc.close()

    file_size = OUTPUT_PDF.stat().st_size
    print(humanize.naturalsize(file_size))
