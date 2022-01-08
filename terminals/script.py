import os
import platform
from datetime import datetime, timezone
from pathlib import Path

from pytablewriter import MarkdownTableWriter
from pytablewriter.typehint import String
from rapidjson import DM_ISO8601, WM_PRETTY, dump, load

DEFAULT_CELL_VALUE: str = "-"
TERM_VAR: str = "TERM"
TERM_PROGRAM_VAR: str = "TERM_PROGRAM"
TERM_PROGRAM_VERSION_VAR: str = "TERM_PROGRAM_VERSION"


def link(text: str, url: str) -> str:
    # More info: https://commonmark.org/help/
    return f"[{text}]({url})"


if __name__ == "__main__":
    term = os.getenv(TERM_VAR, DEFAULT_CELL_VALUE)
    term_program = os.getenv(TERM_PROGRAM_VAR, DEFAULT_CELL_VALUE)
    term_program_version = os.getenv(TERM_PROGRAM_VERSION_VAR, DEFAULT_CELL_VALUE)
    # More info: https://docs.python.org/3.8/library/platform.html#platform.platform
    my_os = platform.platform(terse=True)

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
        value_matrix=[["[]()", term, term_program, term_program_version, my_os]],
        type_hints=[String, String, String, String, String],
        margin=1,
        flavor="github",
    )

    # print(dir(writer))
    # print(writer._MarkdownTableWriter__flavor)

    # writer.write_table()
    output: str = writer.dumps()
    print(output)

    # https://python-rapidjson.readthedocs.io/en/latest/quickstart.html
    # https://python-rapidjson.readthedocs.io/en/latest/dump.html
    # https://python-rapidjson.readthedocs.io/en/latest/load.html
    # https://python-rapidjson.readthedocs.io/en/latest/api.html
    # https://realpython.com/python-json/
    datum = {
        "terminal": "",
        TERM_VAR: term,
        TERM_PROGRAM_VAR: term_program,
        TERM_PROGRAM_VERSION_VAR: term_program_version,
        "os": my_os,
        "timestamp": datetime.now(timezone.utc),
    }

    with open(Path("./data.json"), "r") as fp:
        data = load(fp, datetime_mode=DM_ISO8601)
        # print(data, type(data))

    with open(Path("./data.json"), "w") as fp:
        dump(
            data + [datum],
            fp,
            ensure_ascii=False,
            write_mode=WM_PRETTY,
            indent=2,
            sort_keys=False,
            datetime_mode=DM_ISO8601,
        )
