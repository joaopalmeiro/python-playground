# Check the Python implementation

## [CPython](https://github.com/python/cpython)

- `conda env create -f cpython.yml`
- `conda activate cpython-dev`
- `conda list`
- `python script.py`
- `isort --profile black script.py && black script.py`

## [PyPy](https://www.pypy.org/)

- `conda config --set channel_priority strict`
- `conda create -c conda-forge -n pypy-dev pypy python=3.8`
- `conda activate pypy-dev`
- `conda list`
- `python script.py`

## References

- https://docs.python.org/3.7/library/platform.html#platform.python_implementation
- https://www.python.org/download/alternatives/
- https://www.pypy.org/posts/2022/11/pypy-and-conda-forge.html
- `conda config --show`
