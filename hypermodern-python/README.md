# Hypermodern Python

This folder contains the code for the "[Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)" tutorial series by [Claudio Jolowicz](https://cjolowicz.github.io/).

## Notes

- [pyenv](https://github.com/pyenv/pyenv): Python version manager.
- Make the specified versions of Python available in the repository: `pyenv local 3.8.2 3.7.7`.
- [Poetry](https://python-poetry.org/): Python packaging and dependencies manager (similar to `npm` and `yarn`). Alternatives:
  - [Flit](https://github.com/takluyver/flit).
  - [Pyflow](https://github.com/David-OConnor/pyflow).
  - [DepHell](https://dephell.org/).
- Commands:
  - `poetry init --no-interaction` + `poetry install`.
  - `poetry install` + `poetry run hypermodern-python`.
- The caret (`^`) in front of a version number means "up to the next major release".
- "Use snake case for the package name `hypermodern_python`, as opposed to the kebab case used for the repository name `hypermodern-python`. (...) name the package after your repository, replacing hyphens by underscores."
- The `poetry.lock` file contains the exact versions installed into the virtual environment.

## References

- [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).
