# Color Difference

## Packages

- [scikit-image](https://scikit-image.org/) ([`color`](https://scikit-image.org/docs/stable/api/skimage.color.html) module).
- [colorio](https://github.com/nschloe/colorio).
- [colorspacious](https://github.com/njsmith/colorspacious).
- [python-colormath](https://github.com/gtaylor/python-colormath).
- [Colour](https://github.com/colour-science/colour) ([documentation](https://colour.readthedocs.io/en/latest/)).

## Development

- `pipenv install --python 3.6`.
- `pipenv shell`.

## Notes

- [Color examples to compare](https://colorjs.io/docs/color-difference.html).
- [Old documentation](https://www.colour-science.org/api/0.3.3/html/) for Colour. Current documentation is hosted in Read the Docs since version [0.3.7](https://github.com/colour-science/colour/releases/tag/v0.3.7).
- [Awesome Colour](https://github.com/colour-science/awesome-colour/) (color science resources).
- `pipenv install scikit-image colorio colorspacious colormath colour-science`.
- [Python snippets have been removed from VS Code](https://github.com/microsoft/vscode-python/issues/15279#issuecomment-771306907). They can be found [here](https://github.com/microsoft/vscode-python/blob/2020.12.424452561/snippets/python.json). [Alternative extension](https://marketplace.visualstudio.com/items?itemName=cstrap.python-snippets).
- [HLS](https://en.wikipedia.org/w/index.php?title=HLS_color_space&redirect=no) or HSL color space.
- [`colorsys`](https://docs.python.org/3.6/library/colorsys.html) built-in module.
- [`ImageColor`](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html) module (Pillow).
- [webcolors](https://github.com/ubernostrum/webcolors) package.

### [Color Notebook](https://colorjs.io/notebook/)

```javascript
let color1 = new Color("hsl(30, 100%, 50%)");
let color2 = new Color("hsl(50, 100%, 50%)");
let color3 = new Color("hsl(230, 100%, 50%)");
let color4 = new Color("hsl(260, 100%, 50%)");

color1.deltaE76(color2);
color3.deltaE76(color4);
color2.deltaE76(color3);
```
