import ast
from pathlib import Path

import _pytest.assertion.rewrite as m

code = Path("test.py").read_text()
tree = ast.parse(code)

m.rewrite_asserts(tree, code)

print(ast.unparse(tree))
