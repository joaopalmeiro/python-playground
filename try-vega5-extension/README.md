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

### Issue

When displaying a Vega-Lite chart in JupyterLab or creating a chart with Altair (using the [mimetype renderer](https://altair-viz.github.io/user_guide/display_frontends.html#altair-s-renderer-framework)), the cell output also contains a PNG representation of the chart. Since this representation is created directly from [one of Vega's View API methods](https://vega.github.io/vega/docs/api/view/#view_toImageURL) with only the type argument defined, the `scaleFactor` corresponds to 1, the default value. However, given that it is possible to define a different `scaleFactor` from the [Vega-Embed options](https://github.com/vega/vega-embed#options), if this value is different from 1, it is "ignored" when creating this representation in PNG, as this value is not passed directly when calling the `.toImageURL()` method. The relevant line of code is [this one](https://github.com/jupyterlab/jupyterlab/blob/v3.5.1/packages/vega5-extension/src/index.ts#L136).

### Proposed solution

If you think this flexibility makes sense for this PNG representation, I would also pass the scaleFactor like this (based on [how it's done in Vega-Embed](https://github.com/vega/vega-embed/pull/75)):

```diff
- const imageURL = await this._result.view.toImageURL('png');
+ const imageURL = await this._result.view.toImageURL('png', embedOptions.scaleFactor);
```
