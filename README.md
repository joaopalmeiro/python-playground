# python-playground

Some experiments with [Python](https://www.python.org/).

## Notes

`Snippet` **Abstract base class**

```python
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def talk(self):
        pass
```

---

`Code style` **Underscores in numeric literals**

```python
print(10_000)
```

instead of

```python
print(10000)
```

---

`Snippet` **Prettyprinter for dictionaries**

```python
def print_dict(d: dict, indent: int = 2) -> None:
    from json import dumps

    print(dumps(d, indent=indent))

```

---

`Snippet` **Main function**

```python
def main():
    # Entry point function.
    # Orchestrate the call to other functions here.
    pass

if __name__ == "__main__":
    main()
```

---

`Snippet` **List flattening**

```python
from itertools import chain

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_lst = list(chain.from_iterable(lst))
```

---

`Snippet` **Breakpoint**

```python
import pdb; pdb.set_trace()
```

---

`Snippet` **`frozenset` (immutable and hashable built-in set type)**

```python
d = dict()
x = [1, 2, 3]

fs = frozenset(x)

# It can be used as a dictionary key
d[fs] = 1
```

---

`Snippet` **Empty class**

```python
class Name:
    pass
```

---

`Code style` **Variable names for minimum and maximum values**

```python
data = [1, 2, 3, 4]

# Minimum
mn = min(data)
min_ = min(data)

# Maximum
mx = max(data)
max_ = max(data)
```
