from pathlib import Path

import humanize
from pypdf import PdfWriter

INPUT_PDF = Path("WW5000J_BETTER_SEPM_03793M-00_PT.pdf")
OUTPUT_PDF = Path("out.pdf")

if __name__ == "__main__":
    file_size = INPUT_PDF.stat().st_size
    print(humanize.naturalsize(file_size))

    writer = PdfWriter(clone_from=INPUT_PDF)

    for page in writer.pages:
        page.compress_content_streams()

    writer.compress_identical_objects(remove_identicals=True, remove_orphans=True)

    # After `writer.compress_identical_objects()` to avoid `AttributeError:
    # 'NoneType' object has no attribute 'indirect_reference'`:
    writer.metadata = None

    writer.write(OUTPUT_PDF)

    file_size = OUTPUT_PDF.stat().st_size
    print(humanize.naturalsize(file_size))
