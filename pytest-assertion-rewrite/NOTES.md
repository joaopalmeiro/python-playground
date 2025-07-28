# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://happytest-apidoc.readthedocs.io/en/latest/api/_pytest.assertion.rewrite/
  - https://happytest-apidoc.readthedocs.io/en/latest/_modules/_pytest/assertion/rewrite/#AssertionRewriter.variable:
    - `# Use a character invalid in python identifiers to avoid clashing.`
    - `name = "@py_assert" + str(next(self.variable_counter))`
- https://docs.python.org/3/library/ast.html#ast.unparse
- https://pypy.org/

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
