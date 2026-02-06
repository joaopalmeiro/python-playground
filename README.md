# python-playground

Some experiments with [Python](https://www.python.org/).

## Development

- `pipenv install --python 3.8 && pipenv shell`

## Notes

- [readme.so](https://readme.so/) (online editor to create README files).
- [@vercel/ncc](https://github.com/vercel/ncc): compile a Node.js module into a single file with all its dependencies.
- Check installed packages in Google Colab: `!pip freeze` or `!pip freeze --all` or `!pip list` or `!pip list --format=json` or `!pip list --format=json | python -m json.tool`
  - https://stackoverflow.com/a/47109764
  - https://pip.pypa.io/en/stable/cli/pip_freeze/
  - https://pip.pypa.io/en/stable/cli/pip_list/
  - https://note.nkmk.me/en/python-pip-list-freeze/
- Check the Google Colab release notes: _Help_ > _View release notes_
- [Pyrefly](https://pyrefly.org/):
  - https://pyrefly.org/en/docs/error-kinds/
  - `uvx pyrefly@0.37.0 init --help`
  - `uvx pyrefly@0.37.0 init` or `uvx pyrefly@0.37.0 init pyrefly.toml`
  - `uvx pyrefly@0.37.0 check --summarize-errors`
- [jsonref](https://github.com/gazpachoking/jsonref):
  - https://github.com/simonw/llm/issues/849#issuecomment-2978051802: `replaced = jsonref.replace_refs(schema, lazy_load=False)` + `replaced.pop("$defs")`
  - https://github.com/mathpn/llm-docsmith/issues/4
  - https://github.com/pydantic/pydantic/issues/889
  - https://pypi.org/project/jsonref/
  - https://ai.google.dev/gemini-api/docs/structured-output?example=recipe#json_schema_support
- Install a specific version of PDM using uv: `uv tool install pdm==2.22.2 && pdm --version`
- https://github.com/lucasgelfond/zerobrew
- https://github.com/github/gitignore/blob/53fee13f20a05efc93ef4edcad0c62863520e268/Global/LibreOffice.gitignore: `.~lock.*#`
- https://docs.astral.sh/ty/reference/typing-faq/#does-ty-support-mypy-plugins: "That said, we are considering adding support for popular third-party libraries like pydantic, SQLAlchemy, attrs, or django directly into ty."

### Install any version of PDM via Homebrew

```bash
brew update
```

```bash
brew tap homebrew/core --force
```

```bash
brew tap-new joao-palmeiro/local-formulas
```

```bash
brew extract --version=2.26.0 pdm joao-palmeiro/local-formulas
```

```bash
brew install pdm@2.26.0 && pdm self add keyring
```

```bash
brew uninstall pdm@2.26.0
```

## Snippets

`Snippet` **Abstract base class**

```python
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def talk(self):
        pass
```

---

`Code style` **Underscores in numeric literals**

```python
print(10_000)
```

instead of

```python
print(10000)
```

---

`Snippet` **Prettyprinter for dictionaries**

```python
def print_dict(d: dict, indent: int = 2) -> None:
    from json import dumps

    print(dumps(d, indent=indent))

```

---

`Snippet` **Main function**

```python
def main():
    # Entry point function.
    # Orchestrate the call to other functions here.
    pass

if __name__ == "__main__":
    main()
```

---

`Snippet` **List flattening**

```python
from itertools import chain

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_lst = list(chain.from_iterable(lst))
```

---

`Snippet` **Breakpoint**

```python
import pdb; pdb.set_trace()
```

---

`Snippet` **`frozenset` (immutable and hashable built-in set type)**

```python
d = dict()
x = [1, 2, 3]

fs = frozenset(x)

# It can be used as a dictionary key
d[fs] = 1
```

---

`Snippet` **Empty class**

```python
class Name:
    pass
```

---

`Code style` **Variable names for minimum and maximum values**

```python
data = [1, 2, 3, 4]

# Minimum
mn = min(data)
min_ = min(data)

# Maximum
mx = max(data)
max_ = max(data)
```

---

`Tooling` **Create a Pipenv environment with the `.venv` folder locally and a specific `pip` version**

```bash
export PIPENV_VENV_IN_PROJECT=1 && \
export VIRTUALENV_PIP=22.0.2 && \
export VIRTUALENV_DOWNLOAD=1 && \
pipenv install --python 3.7 --dev
```

Note: `VIRTUALENV_DOWNLOAD` may not be necessary. In my case, it was necessary to ensure that Pipenv was using a newer version.

- [virtualenv CLI flags](https://virtualenv.pypa.io/en/latest/cli_interface.html#section-seeder)
- [GitHub issue](https://github.com/pypa/pipenv/issues/3142#issuecomment-831378235)

---

`Snippet` **`.vscode/settings.json` file**

```json
{
  "editor.formatOnSave": true,

  "python.formatting.provider": "black",

  "python.linting.enabled": true,
  "python.linting.lintOnSave": true,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": ["--ignore=E501,W503"],
  "python.linting.mypyEnabled": true,

  "python.sortImports.args": ["--atomic"],

  "[python]": {
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```
