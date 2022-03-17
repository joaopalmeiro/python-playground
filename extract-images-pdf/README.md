# Extract images from PDF

## Development

- `pipenv install --python 3.7`.
- `pipenv run python extract_img.py`.

## Notes

- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) package.
- [pdfminer.six](https://pdfminersix.readthedocs.io/en/latest/index.html) package:
  - `pipenv install pdfminer.six`.
  - [How to extract images from a PDF](https://pdfminersix.readthedocs.io/en/latest/howto/images.html).
  - `pipenv run pdf2txt.py 2107.11367.pdf --output-dir paper`. [API](https://pdfminersix.readthedocs.io/en/latest/reference/commandline.html).
