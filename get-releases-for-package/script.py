import requests
from dateutil import parser
from packaging.version import parse
from rich.console import Console
from rich.table import Table

# from rich import print_json

# https://github.com/pypa/packaging
# https://packaging.pypa.io/en/latest/version.html
# https://packaging.pypa.io/en/latest/version.html#packaging.version.Version
def is_final_version(version: str) -> bool:
    parsed_version = parse(version)

    return not parsed_version.is_prerelease and not parsed_version.is_postrelease


PACKAGE: str = "Sphinx"
BASE_URL: str = f"https://pypi.org/project/{PACKAGE}"

if __name__ == "__main__":
    # https://warehouse.pypa.io/api-reference/json.html
    # https://requests.readthedocs.io/en/latest/user/advanced/#session-objects
    with requests.Session() as s:
        res = s.get(f"https://pypi.org/pypi/{PACKAGE}/json")
        data = res.json()

    # print_json(res.text)
    # print(data.keys())
    # print(data["releases"].keys())
    # https://www.willmcgugan.com/blog/tech/post/pretty-printing-json-with-rich/
    # https://pypi.org/project/Sphinx/5.3.0/
    # https://pypi.org/project/Sphinx/0.1.61611/
    # print_json(data=data["releases"]["5.3.0"])
    # print_json(data=data["releases"]["1.3b3"])
    # print_json(data=data["releases"]["0.1.61611"])

    # https://stackoverflow.com/a/45253740
    # all_versions = [*data["releases"]]
    # print(all_versions)

    # https://python-semver.readthedocs.io/en/stable/api.html#semver.parse
    # https://github.com/python-semver/python-semver
    # https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions

    # https://peps.python.org/pep-0440/: PEP 440 — Version Identification and Dependency Specification
    # https://peps.python.org/pep-0440/#semantic-versioning
    # https://peps.python.org/pep-0440/#final-releases
    # https://python-semver.readthedocs.io/en/latest/advanced/convert-pypi-to-semver.html
    final_versions = [
        version for version in data["releases"] if is_final_version(version)
    ]
    # print(final_versions)

    # https://rich.readthedocs.io/en/stable/tables.html
    table = Table(title=PACKAGE, show_lines=True)
    table.add_column("Version")
    table.add_column("Date")
    table.add_column("PyPI URL")

    # https://docs.python.org/3.7/library/datetime.html#datetime.datetime.fromisoformat
    # https://stackoverflow.com/a/3908349
    # https://stackoverflow.com/a/969324
    # https://dateutil.readthedocs.io/en/stable/parser.html#dateutil.parser.isoparse
    for version in final_versions:
        files = data["releases"][version]
        dts = [parser.isoparse(file["upload_time_iso_8601"]) for file in files]
        ref_dt = min(dts)
        fmt_dt = ref_dt.strftime("%b %d, %Y")

        url = f"{BASE_URL}/{version}/"

        table.add_row(version, fmt_dt, url)

    console = Console()
    console.print(table, justify="center")
