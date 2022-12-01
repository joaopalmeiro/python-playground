# Check if dependencies exist in `Pipfile.lock` files

## Development

- `pipenv install --python 3.7`
- `pipenv run python script.py`
- `pipenv run isort --profile black script.py && pipenv run black script.py`

## References

- https://github.com/pypa/pipfile
- https://github.com/pypa/pipfile/blob/main/pipfile/api.py#L20
- https://github.com/pypa/pipfile#examples-spec-v6

## Notes

- `pipenv install black isort rich`
