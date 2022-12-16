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
- https://nbviewer.org/github/joaopalmeiro/python-playground/blob/master/try-vega5-extension/dev.ipynb

## Notes

- `conda deactivate` + `conda env remove --name try-vega5-extension`
- Development environment for JupyterLab ([documentation](https://jupyterlab.readthedocs.io/en/latest/developer/contributing.html#setting-up-a-local-development-environment)):
  - `conda create -c conda-forge -n jlab-dev python=3.8 nodejs pkg-config pango libpng cairo jpeg giflib librsvg glib`
    - Note: Use Python 3.8 instead of 3.7 because of Flake8.
  - `conda activate jlab-dev`
  - `conda env config vars list`
  - `conda env config vars set PKG_CONFIG_PATH=$CONDA_PREFIX/lib/pkgconfig`
  - `conda activate jlab-dev`
  - `conda env config vars list`
  - From the cloned JupyterLab repo folder:
    - `pip install -e ".[dev,test]"`
    - `jlpm install`
    - `jlpm run build`
    - `jupyter lab --dev-mode` or `jupyter lab --dev-mode --watch`
    - `jlpm run build:testutils`
    - `jlpm test`
    - `pip install pre-commit`
    - `pre-commit install`
    - `pre-commit run`
  - `conda deactivate` + `conda env remove --name jlab-dev`

### Issue

When displaying a Vega-Lite chart in JupyterLab or creating a chart with Altair (using the [mimetype renderer](https://altair-viz.github.io/user_guide/display_frontends.html#altair-s-renderer-framework)), the cell output also contains a PNG representation of the chart. Since this representation is created directly from [one of Vega's View API methods](https://vega.github.io/vega/docs/api/view/#view_toImageURL) with only the type argument defined, the `scaleFactor` corresponds to 1, the default value. However, given that it is possible to define a different `scaleFactor` from the [Vega-Embed options](https://github.com/vega/vega-embed#options), if this value is different from 1, it is "ignored" when creating this representation in PNG, as this value is not passed directly when calling the `.toImageURL()` method. The relevant line of code is [this one](https://github.com/jupyterlab/jupyterlab/blob/v3.5.1/packages/vega5-extension/src/index.ts#L136).

### Proposed solution

If you think this flexibility makes sense for this PNG representation, I would also pass the scaleFactor like this (based on [how it's done in Vega-Embed](https://github.com/vega/vega-embed/pull/75)):

```diff
- const imageURL = await this._result.view.toImageURL('png');
+ const imageURL = await this._result.view.toImageURL('png', embedOptions.scaleFactor);
```

## Snippets

```python
from IPython.display import display

display(
    {
        "application/vnd.vegalite.v4+json": {
            "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
            "description": "A simple bar chart with embedded data.",
            "data": {
                "values": [
                    {"a": "A", "b": 28},
                    {"a": "B", "b": 55},
                    {"a": "C", "b": 43},
                    {"a": "D", "b": 91},
                    {"a": "E", "b": 81},
                    {"a": "F", "b": 53},
                    {"a": "G", "b": 19},
                    {"a": "H", "b": 87},
                    {"a": "I", "b": 52},
                ]
            },
            "mark": "bar",
            "encoding": {
                "x": {"field": "a", "type": "nominal", "axis": {"labelAngle": 0}},
                "y": {"field": "b", "type": "quantitative"},
            },
        }
    },
    raw=True,
)
```

```python
from IPython.display import display

display(
    {
        "application/vnd.vegalite.v4+json": {
            "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
            "description": "A simple bar chart with embedded data.",
            "data": {
                "values": [
                    {"a": "A", "b": 28},
                    {"a": "B", "b": 55},
                    {"a": "C", "b": 43},
                    {"a": "D", "b": 91},
                    {"a": "E", "b": 81},
                    {"a": "F", "b": 53},
                    {"a": "G", "b": 19},
                    {"a": "H", "b": 87},
                    {"a": "I", "b": 52},
                ]
            },
            "mark": "bar",
            "encoding": {
                "x": {"field": "a", "type": "nominal", "axis": {"labelAngle": 0}},
                "y": {"field": "b", "type": "quantitative"},
            },
        }
    },
    metadata={
        "application/vnd.vegalite.v4+json": {
            "embed_options": {
                "scaleFactor": 5,
            }
        }
    },
    raw=True,
)
```
