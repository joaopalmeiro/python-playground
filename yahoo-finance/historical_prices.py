import json
import time
from typing import Any, Dict, List, Sequence, Union

import pandas as pd
import requests

BASE_URL = "https://query1.finance.yahoo.com/v8/finance/chart/"


def jprint(obj, indent=4, ensure_ascii=False):
    print(json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii))


def get_historical_prices(
    symbol: str,
    start: str = "2010-01-01",
    end: str = "2021-01-01",
    date_fmt: str = "%Y-%m-%d",
    granularity: str = "1d",
    verbose: bool = False,
):
    start_unix_secs = int(time.mktime(time.strptime(start, date_fmt)))
    end_unix_secs = int(time.mktime(time.strptime(end, date_fmt)))

    params: Dict[str, Union[int, str]] = {
        "period1": start_unix_secs,
        "period2": end_unix_secs,
        "interval": granularity,
    }

    url = f"{BASE_URL}{symbol}"

    data = requests.get(url=url, params=params)

    if verbose:
        print(f"URL: {data.url}\n")

    return data.json()


def parse_historical_prices(
    data: Dict[str, Any], rounding: bool = True
) -> pd.DataFrame:
    data_to_parse = data["chart"]["result"][0]

    symbol = data_to_parse["meta"]["symbol"]
    currency = data_to_parse["meta"]["currency"]

    timestamps = data_to_parse["timestamp"]
    ohlc = data_to_parse["indicators"]["quote"][0]  # OHLC: open-high-low-close

    opens = ohlc["open"]
    lows = ohlc["low"]
    highs = ohlc["high"]
    volumes = ohlc["volume"]
    closes = ohlc["close"]

    adjcloses = data_to_parse["indicators"]["adjclose"][0]["adjclose"]

    parsed_data = pd.DataFrame(
        {
            "symbol": symbol,
            "date": pd.to_datetime(timestamps, origin="unix", unit="s").normalize(),
            "open": opens,
            "high": highs,
            "low": lows,
            "close": closes,
            "adj_close": adjcloses,
            "volume": volumes,
            "currency": currency,
        }
    )

    if rounding:
        decimals = data_to_parse["meta"]["priceHint"]
        cols = ["open", "high", "low", "close", "adj_close"]

        parsed_data[cols] = parsed_data[cols].round(decimals)

    return parsed_data


def get_dataset(
    symbols: Union[str, Sequence[str]],
    start: str = "2010-01-01",
    end: str = "2021-01-01",
    date_fmt: str = "%Y-%m-%d",
    granularity: str = "1d",
    verbose: bool = False,
    rounding: bool = True,
) -> pd.DataFrame:
    symbols = [symbols] if isinstance(symbols, str) else symbols

    all_data: List[pd.DataFrame] = []

    for symbol in symbols:
        raw_data = get_historical_prices(
            symbol,
            start=start,
            end=end,
            date_fmt=date_fmt,
            granularity=granularity,
            verbose=verbose,
        )

        data = parse_historical_prices(raw_data, rounding=rounding)

        all_data.append(data)

    return pd.concat(all_data).reset_index(drop=True)
