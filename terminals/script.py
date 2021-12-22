import os
import platform

from pytablewriter import MarkdownTableWriter
from pytablewriter.typehint import String

DEFAULT_CELL_VALUE: str = "-"
TERM_VAR: str = "TERM"
TERM_PROGRAM_VAR: str = "TERM_PROGRAM"
TERM_PROGRAM_VERSION_VAR: str = "TERM_PROGRAM_VERSION"


def link(text: str, url: str) -> str:
    # More info: https://commonmark.org/help/
    return f"[{text}]({url})"


if __name__ == "__main__":
    # More info:
    # - https://pytablewriter.readthedocs.io/en/latest/pages/reference/writers/text/markup/md.html
    # - https://pytablewriter.readthedocs.io/en/latest/pages/examples/table_format/text/markdown.html#example-markdown-table-writer
    # - https://pytablewriter.readthedocs.io/en/latest/pages/examples/typehint/python.html#example-type-hint-python
    # - https://pytablewriter.readthedocs.io/en/latest/pages/examples/output/dump/index.html
    writer = MarkdownTableWriter(
        headers=[
            "Terminal",
            TERM_VAR,
            TERM_PROGRAM_VAR,
            TERM_PROGRAM_VERSION_VAR,
            "OS",
        ],
        value_matrix=[
            [
                "[]()",
                os.getenv(TERM_VAR, DEFAULT_CELL_VALUE),
                os.getenv(TERM_PROGRAM_VAR, DEFAULT_CELL_VALUE),
                os.getenv(TERM_PROGRAM_VERSION_VAR, DEFAULT_CELL_VALUE),
                # More info: https://docs.python.org/3.8/library/platform.html#platform.platform
                platform.platform(terse=True),
            ]
        ],
        type_hints=[String, String, String, String, String],
        margin=1,
        flavor="github",
    )

    # print(dir(writer))
    # print(writer._MarkdownTableWriter__flavor)

    # writer.write_table()
    output: str = writer.dumps()
    print(output)
