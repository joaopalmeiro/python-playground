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
