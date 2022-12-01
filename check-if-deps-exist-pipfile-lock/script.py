import json

MARKDOWN_PARSERS = [
    # https://github.com/miyuchina/mistletoe
    # https://pypi.org/project/mistletoe/
    "mistletoe",
    # https://github.com/lepture/mistune
    # https://pypi.org/project/mistune/
    "mistune",
]

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

    for package in MARKDOWN_PARSERS:
        if package in packages:
            print(f"{package} {packages[package]['version']}")
        else:
            print(f"No {package}")
