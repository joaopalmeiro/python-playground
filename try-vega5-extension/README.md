# Try `@jupyterlab/vega5-extension`

## Development

- `conda env create -f environment.yml`
- `conda activate try-vega5-extension`
- `jupyter lab`
- `python dev.py`
- `black dev.ipynb`
- `isort dev.py && black dev.py`

## References

- https://github.com/jupyterlab/jupyterlab/tree/v3.5.1/packages/vega5-extension
- https://github.com/vega/vega-embed/pull/75
- https://github.com/vega/vega-embed/issues/73
- https://vega.github.io/vega/docs/api/view/#view_toImageURL
- https://vega.github.io/vega-lite/examples/bar.html or https://vega.github.io/vega-lite-v4/examples/bar.html
- https://github.com/vega/vega-embed

## Notes

- `conda deactivate` + `conda env remove --name try-vega5-extension`
