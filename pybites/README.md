# PyBites Python Tips

## Notes

- Swap 2 variables: tuple unpacking.
- `enumerate(iterable, start=1)`.
- `sorted(string_iterable, key=str.lower)`.
- `==` (same content/value) vs. `is` (same object).
- `id()` can be used to check if different variables refer to the same object.
- `.__mro__` (get an object's inheritance tree).
- When using `in` against a `list`, all items are checked sequentially (slower). Against a `set`, a hashable type, lookups are faster.
- `with open("hello", "x") as f:`: the `"x"` mode is for exclusive creation, failing if the file already exists.
- Strip punctuation: `from string import punctuation` + `table = str.maketrans({key: None for key in punctuation})` + `my_string.translate(table)`.
- `from pprint import pprint as pp`.
- `collections.ChainMap`: group multiple dictionaries/mappings. It allows you to create a precedence chain, where the first argument takes precedence over the second and so on (e.g., `ChainMap(cli_args, os.environ, defaults)`).
- `from contextlib import redirect_stdout`:
  - Context manager for redirecting standard output.
  - `with redirect_stdout(sys.stderr):`: redirect output to standard error.
- `from distutils.version import StrictVersion`: compare version numbers (e.g., `StrictVersion('0.10.1') < StrictVersion('1.0.3')`).
- `inspect.cleandoc(doc)`: clean up indentation from docstrings.
- `from bisect import insort`: insert items in a list in sorted order.
- `?` after the qualifier (e.g., `*?`) makes it perform the match in _non-greedy_ or _minimal_ fashion.
- `p help(...)`: call `help()` inside [pdb](https://docs.python.org/3/library/pdb.html).
- `python -m json.tool <file>.json`: CLI to validate and pretty-print JSON objects.
- `Path.glob`.
- `str.casefold`: similar to `str.lower` and intended to remove all case distinctions in a string.
- `with open("f1.txt") as f1, open("f2.txt") as f2:`: open two files.
- It is possible to round to the next 10, 100, 1000 and so on by defining a negative `ndigits` argument for the `round()` function.

## Packages

- [TextBlob](https://textblob.readthedocs.io/en/dev/) (a package for text processing and NLP).
- [requests-cache](https://requests-cache.readthedocs.io/en/latest/index.html) (a package for caching API calls).
- [packaging](https://packaging.pypa.io/en/latest/) (a package with core utilities for Python packages).
- [imageio](https://imageio.github.io/) (a package for reading and writing image data).
- [Python-Markdown](https://python-markdown.github.io/).
- [howdoi](https://github.com/gleitz/howdoi) (a CLI to get answers from Stack Overflow).
- [ipykernel](https://ipykernel.readthedocs.io/en/latest/) (it allows the installation of a dedicated kernel for a virtual environment).
