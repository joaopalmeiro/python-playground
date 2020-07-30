import pandas as pd
from pandas.api.extensions import register_dataframe_accessor
from re import sub

TO_NORMALIZE = [(r"[ ()]", "_")]


@register_dataframe_accessor("clean")
class CleanAccessor:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(obj):
        if not isinstance(obj, pd.DataFrame):
            raise AttributeError("It must be a pandas DataFrame.")

    @staticmethod
    def _lower_case(col):
        return col.lower()

    @staticmethod
    def _normalize(col):
        for search, replace in TO_NORMALIZE:
            col = sub(search, replace, col)

        return col

    @staticmethod
    def _remove_extra_underscores(col):
        return sub(r"_+", "_", col)

    @staticmethod
    def _strip_underscores(col):
        return col.strip("_")

    def column_names(self):
        return (
            self._obj.rename(columns=self._lower_case)
            .rename(columns=self._normalize)
            .rename(columns=self._remove_extra_underscores)
            .rename(columns=self._strip_underscores)
        )
