import requests
from rich import print_json

PACKAGE = "sphinx"

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
    print_json(data=data["releases"]["5.3.0"])
