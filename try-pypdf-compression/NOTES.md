# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- pypdf:
  - https://pypi.org/project/pypdf/
  - https://pypdf.readthedocs.io/en/stable/user/file-size.html
    - "It is recommended to apply this process [(`writer.compress_identical_objects()`)] just before writing to the file/stream."
    - https://docs.python.org/3/library/zlib.html#zlib.compress
  - https://www.youtube.com/watch?v=tgOABUhVwFs
  - https://pypdf.readthedocs.io/en/stable/user/metadata.html#removing-metadata-entry
  - https://pypdf.readthedocs.io/en/stable/user/extract-images.html
- https://github.com/Warraybe/optimize_pdf/blob/db88c23425f06352b6a1039c2d65f8f9a4a144aa/optimize_pdf.py#L13-L49
- https://github.com/GabrielPMagni/PyReducePdf/blob/7c0774ba3eaf0875db37a39abfe55388d48086ee/app.py#L64-L81
- PyMuPDF:
  - https://pymupdf.readthedocs.io/en/latest/document.html#Document.subset_fonts
  - https://pymupdf.readthedocs.io/en/latest/document.html#Document.save
  - https://pymupdf.readthedocs.io/en/latest/document.html#Document.ez_save
  - https://pymupdf.readthedocs.io/en/latest/document.html#set-metadata-example
  - https://pymupdf.readthedocs.io/en/latest/recipes-images.html#how-to-make-images-from-document-pages
  - https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_pixmap
- https://github.com/mapbox/pixelmatch
- https://artifex.com/licensing
  - https://github.com/browser-use/browser-use/issues/2610

## Commands

```bash
deactivate && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
npx pixelmatch@7.1.0 img/input/page-0.png img/output/page-0.png img/diff-0.png 0.1
```

```bash
for file in img/input/*.png; do
  filename=$(basename "$file")
  npx pixelmatch@7.1.0 "img/input/$filename" "img/output/$filename" "img/diff-${filename#page-}" 0.1
done
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```
