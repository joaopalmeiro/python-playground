# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://github.com/lincolnloop/python-qrcode
  - https://pypi.org/project/qrcode/

## Commands

```bash
deactivate && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```
