# Try Aequitas

## Development

- `pipenv install --python 3.7`
- `pipenv run jupyter lab`
- `pipenv run nbqa isort dev.ipynb --float-to-top`
- `pipenv run black dev.ipynb`

## Notes

- [Repo](https://github.com/dssg/aequitas)
- `pipenv install nbqa isort`
- [ColorAide](https://github.com/facelessuser/coloraide) package ([documentation](https://facelessuser.github.io/coloraide/))
- Development environment for Aequitas:
  - `conda create --no-default-packages --override-channels --channel conda-forge --name aequitas-dev python=3.7 pip=22.0.2 jupyterlab=3.2.5`
  - `conda activate aequitas-dev`
  - `conda list`
  - `pip install -e .`
  - `conda list`
  - `conda env remove --name aequitas-dev`
- https://conda.io/projects/conda/en/latest/commands/create.html
- https://conda.io/projects/conda/en/latest/commands/list.html: `conda list --json`
- `ModuleNotFoundError: No module named 'scipy'`:
  - https://github.com/dssg/aequitas/blob/0.42.0/src/aequitas/bias.py#L6
  - https://github.com/dssg/aequitas/blob/0.42.0/requirement/main.txt (`pandas>=0.24.1`)
  - https://pandas.pydata.org/pandas-docs/version/0.24.1/install.html
  - https://github.com/pandas-dev/pandas/blob/v0.24.1/doc/source/install.rst#optional-dependencies (`scipy>=0.18.1`)
