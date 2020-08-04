from dataclasses import dataclass  # Available from Python 3.7
from typing import Any


@dataclass
class DataClassCard:
    rank: str
    suit: str


# vs.


class ClassCard:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(rank={self.rank!r}, suit={self.suit!r})"  # `!r` -> `repr()`

    def __eq__(self, other: Any) -> bool:
        if other.__class__ is not self.__class__:
            # More info: https://docs.python.org/3.6/library/constants.html#NotImplemented
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


dataclass_card = DataClassCard("Q", "Hearts")
class_card = ClassCard("Q", "Hearts")

print(dataclass_card)
print(class_card)

print(dataclass_card == DataClassCard("Q", "Hearts"))
print(class_card == ClassCard("Q", "Hearts"))
