# python-playground

Some experiments with [Python](https://www.python.org/).

## Notes

`Snippet` **Abstract Base Class**

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

`Code style` **Underscores in Numeric Literals**

```python
print(10_000)
```

instead of

```python
print(10000)
```

---

`Snippet` **Prettyprinter for Dictionaries**

```python
def print_dict(d: dict, indent: int = 2) -> None:
    from json import dumps

    print(dumps(d, indent=indent))

```

---

`Snippet` **Main Function**

```python
def main():
    # Entry point function.
    # Orchestrate the call to other functions here.
    pass

if __name__ == "__main__":
    main()
```

---

`Snippet` **List Flattening**

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
