import json
import time
from typing import Any, Dict, Union

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
        print("URL:", data.url)

    return data.json()


def parse_historical_prices(data: Dict[str, Any]) -> pd.DataFrame:
    pass


if __name__ == "__main__":
    raw_data = get_historical_prices(
        "MSFT", start="2019-04-15", end="2019-04-17", verbose=True
    )
