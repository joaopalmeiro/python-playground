# Try nbproject

## Notes

- [Installation](https://lamin.ai/docs/nbproject)
- [GitHub repo](https://github.com/laminlabs/nbproject)
- It uses [ipylab](https://github.com/jtpio/ipylab)
- `pipenv install jupyterlab nbproject`
- `pipenv run nb-clean clean demo.ipynb`
- `pipenv run nb-clean check demo.ipynb`
- `pipenv run jupyter nbconvert --version`

## Development

- `pipenv install --python 3.7`
- `pipenv run jupyter lab`
- Clean notebook: `pipenv run jupyter nbconvert --ClearMetadataPreprocessor.enabled=True --to=notebook --inplace demo.ipynb`
  - https://github.com/jupyter/nbconvert/blob/7.0.0/nbconvert/preprocessors/clearmetadata.py#L11
  - https://nbconvert.readthedocs.io/en/7.0.0/api/preprocessors.html
  - https://nbconvert.readthedocs.io/en/7.0.0/usage.html#notebook-and-preprocessors
