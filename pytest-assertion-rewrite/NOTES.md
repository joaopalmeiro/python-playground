# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://happytest-apidoc.readthedocs.io/en/latest/api/_pytest.assertion.rewrite/
  - "Rewrite assertion AST to produce nice error messages"
  - https://happytest-apidoc.readthedocs.io/en/latest/_modules/_pytest/assertion/rewrite/#AssertionRewriter.variable:
    - `# Use a character invalid in python identifiers to avoid clashing.`
    - `name = "@py_assert" + str(next(self.variable_counter))`
  - https://happytest-apidoc.readthedocs.io/en/latest/api/_pytest._io.saferepr/
- https://docs.python.org/3/library/ast.html#ast.unparse
- https://pypy.org/
- https://aider.chat/2024/12/21/polyglot.html

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
