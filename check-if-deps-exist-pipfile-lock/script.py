import json

from packaging.utils import canonicalize_name
from rich.console import Console
from rich.table import Table

MARKDOWN_PARSERS = [
    # https://github.com/miyuchina/mistletoe
    # https://pypi.org/project/mistletoe/
    "mistletoe",
    # https://github.com/lepture/mistune
    # https://pypi.org/project/mistune/
    "mistune",
    # https://github.com/frostming/marko
    # https://pypi.org/project/marko/
    "marko",
    # https://github.com/Python-Markdown/markdown
    # https://pypi.org/project/Markdown/
    "Markdown",
    # "six",
    # "alabaster",
    # "Sphinx",
]

ROW_STYLES = {"default": "green", "develop": "yellow", "default, develop": "green"}

BASE_URL = "https://pypi.org/project"

if __name__ == "__main__":
    with open("data/Pipfile.lock", "r") as f:
        data = json.load(f)

    # print(data.keys())

    # https://github.com/pypa/pipfile#examples-spec-v6
    # https://github.com/pypa/pipfile/blob/main/pipfile/api.py#L132
    spec = data["_meta"]["pipfile-spec"]
    # print(spec)

    # https://github.com/pypa/pipfile/blob/main/pipfile/api.py#L83
    packages = data["default"]
    dev_packages = data["develop"]

    # print(packages.keys())
    # print(dev_packages.keys())

    # https://stackoverflow.com/a/18554039
    # intersection = packages.keys() & dev_packages.keys()
    # print(intersection)
    # for package in intersection:
    #     print(
    #         packages[package]["version"],
    #         dev_packages[package]["version"],
    #         packages[package]["version"] == dev_packages[package]["version"],
    #     )

    # https://rich.readthedocs.io/en/stable/tables.html
    table = Table(title="Pipfile.lock", show_lines=True)
    table.add_column("Package")
    table.add_column("Dependency")
    table.add_column("Version")
    table.add_column("Groups")
    table.add_column("PyPI URL")

    for package in MARKDOWN_PARSERS:
        # https://packaging.pypa.io/en/latest/utils.html#packaging.utils.canonicalize_name
        normalized_package = canonicalize_name(package)
        # print(package, normalized_package)

        dependency = "No"
        version = "-"
        group = "-"
        pypi_url = "-"

        if normalized_package in packages:
            dependency = "Yes"
            version = packages[normalized_package]["version"]
            group = "default"
            pypi_url = f"{BASE_URL}/{package}/{version.lstrip('=')}/"

        if normalized_package in dev_packages:
            if dependency == "Yes":
                group = f"{group}, develop"
            else:
                dependency = "Yes"
                version = dev_packages[normalized_package]["version"]
                group = "develop"
                pypi_url = f"{BASE_URL}/{package}/{version.lstrip('=')}/"

        # https://rich.readthedocs.io/en/stable/reference/table.html#rich.table.Table.add_row
        row_style = ROW_STYLES[group] if dependency == "Yes" else None
        table.add_row(
            normalized_package, dependency, version, group, pypi_url, style=row_style
        )

    console = Console()
    console.print(table)
