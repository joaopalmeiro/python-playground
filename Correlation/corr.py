from bisect import bisect_left, bisect_right
from math import sqrt
from typing import List, Union

import numpy as np
import pandas as pd
from pandas._testing import assert_series_equal
from scipy.stats import rankdata


def pearson_corr(x: np.ndarray, y: np.ndarray) -> np.float64:
    mean_x = x.mean()
    mean_y = y.mean()

    xm = x - mean_x
    ym = y - mean_y

    numerator = (xm * ym).sum()
    denominator = sqrt((xm ** 2).sum()) * sqrt((ym ** 2).sum())

    corr = numerator / denominator

    return corr


def compare_rank_data_methods(
    data: pd.DataFrame, col: str, method: str = "first"
) -> pd.DataFrame:
    df_compare = pd.DataFrame()

    data_nan = data.dropna(subset=[col])
    df_compare[col] = data_nan[col]

    df_compare["pandas"] = data_nan[col].rank(
        method="first" if method == "ordinal" else method
    )

    df_compare["scipy"] = rankdata(
        data_nan[col], method="ordinal" if method == "first" else method
    )

    assert_series_equal(
        df_compare["pandas"], df_compare["scipy"], check_dtype=False, check_names=False
    )

    return df_compare


def get_item_average_rank(
    item: Union[np.float64, float], lst: List[float], np_mode: bool, start: int
) -> Union[np.float64, float]:
    # Locate the insertion point for `item` in `x` to maintain sorted order.

    if np_mode:
        # The `start` value is important because the values obtained through
        # the bisect range from `0` to `len(lst)` (and not to `len(lst) - 1`).

        # The mid-range (in this case for the indexes) is the arithmetic mean
        # of the highest and lowest values of a set: M = (max + min) / 2
        return (
            start
            + np.searchsorted(lst, item, side="left")
            + np.searchsorted(lst, item, side="right")
        ) / 2

    return (start + bisect_left(lst, item) + bisect_right(lst, item)) / 2


def average_rank(
    lst: Union[np.ndarray, List[float]], np_mode: bool = True, start: int = 1
) -> Union[np.ndarray, List[float]]:
    # The sum of the ranking positions is the same as under ordinal ranking.

    sorted_lst = sorted(lst)
    ranking = [get_item_average_rank(i, sorted_lst, np_mode, start) for i in lst]

    return np.array(ranking) if np_mode else ranking


def spearman_corr(x: np.ndarray, y: np.ndarray) -> np.float64:
    xsort = average_rank(x, np_mode=True)
    ysort = average_rank(y, np_mode=True)

    corr = pearson_corr(xsort, ysort)

    return corr
