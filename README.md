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
print(10000)
print(10_000)
```
