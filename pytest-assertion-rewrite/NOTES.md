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
- https://github.com/homeport/termshot
  - https://github.com/sharkdp/bat
  - https://pygments.org/docs/cmdline/
- https://www.linkedin.com/posts/daniel-vila-suero-484b6b45_hugging-face-jobs-are-here-run-any-activity-7355612502597992448-1lPa
  - https://huggingface.co/docs/huggingface_hub/guides/jobs
  - https://huggingface.co/uv-scripts
- https://benmyers.dev/blog/code-snippet-alt-text/

## Commands

```bash
deactivate && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
termshot --filename test_code.png -- "bat test.py"
```

```bash
uvx --from 'Pygments==2.19.2' pygmentize --help
```

```bash
termshot --filename test_code.png -- "uvx --from 'Pygments==2.19.2' pygmentize -O style=github-dark test.py"
```

```bash
termshot --filename internal_pytest_code.png -- "uvx --from 'Pygments==2.19.2' pygmentize -O style=nord 01.py"
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```
