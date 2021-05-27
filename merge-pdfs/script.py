from typing import List, Tuple

import click
from PyPDF2 import PageRange, PdfFileMerger


def merge_pdfs(
    filenames: Tuple[str, ...], page_ranges: List[PageRange], output_filename: str,
) -> None:
    # Source: https://stackoverflow.com/a/37945454

    # Documentation:
    # - https://pythonhosted.org/PyPDF2/PdfFileMerger.html
    # - https://pythonhosted.org/PyPDF2/Easy%20Concatenation%20Script.html#page-range
    merger = PdfFileMerger()

    for pdf, page_range in zip(filenames, page_ranges):
        merger.append(pdf, pages=page_range)

    merger.write(output_filename)
    merger.close()


@click.command()
@click.argument(
    "files",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=str),
    nargs=-1,
)
@click.option(
    "-o",
    "--output-file",
    type=str,
    help="The filename of the final merged PDF.",
    default="merged.pdf",
    metavar="FILE",
    show_default=True,
)
def cli(files: Tuple[str, ...], output_file: str) -> None:
    """Merge the PDF [FILES]."""
    # Documenting scripts: https://click.palletsprojects.com/en/8.0.x/documentation/
    page_ranges = [
        PageRange(
            click.prompt(
                f"\nPlease enter a valid {click.style('page range', bold=True)} for {repr(file)}",
                type=str,
            )
        )
        for file in files
    ]

    merge_pdfs(files, page_ranges, output_file)

    click.secho("\n✨ Done!", bold=True)


if __name__ == "__main__":
    cli()
