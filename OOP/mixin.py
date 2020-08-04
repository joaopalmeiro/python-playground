#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from abc import ABC


class color:
    BOLD = "\033[1m"
    END = "\033[0m"


class TotalBillMixin:
    def total_bill(self):
        divider = "-" * len(self.slices)
        total_price = 0
        bill = ""

        for s in self.slices:
            total_price += s.bill(self)[1]
            bill += f"{s.bill(self)[0]} €{s.bill(self)[1]}\n"

        return f"\n{color.BOLD}Bill{color.END}:\n\n{bill}{divider}\n{'€' + str(total_price):>6}\n"


class Item(ABC):
    def __init__(self, name=None, emoji=None):
        self._name = name
        self._emoji = emoji


class Slice(Item):
    def __init__(self, name, emoji, price):
        super().__init__(name, emoji)
        self._price = price

    def bill(self):
        return (self._emoji, self._price)


class Pizza(Slice, TotalBillMixin):
    def __init__(self, n_slices):
        super().__init__("Slice of Pizza", "\U0001F355", 2)
        self.slices = [Slice] * n_slices


pizza = Pizza(6)
print(pizza.total_bill())
