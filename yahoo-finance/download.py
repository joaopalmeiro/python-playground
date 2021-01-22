import time
from typing import Dict, Union

import requests

BASE_URL = "https://query1.finance.yahoo.com/v8/finance/chart/"


def historical_prices(
    symbol: str,
    start: str = "2010-01-01",
    end: str = "2021-01-01",
    date_fmt: str = "%Y-%m-%d",
    interval: str = "1d",
):
    start_unix_secs = int(time.mktime(time.strptime(start, date_fmt)))
    end_unix_secs = int(time.mktime(time.strptime(end, date_fmt)))

    params: Dict[str, Union[int, str]] = {
        "period1": start_unix_secs,
        "period2": end_unix_secs,
        "interval": interval,
    }

    url = f"{BASE_URL}{symbol}"

    data = requests.get(url=url, params=params)

    return data.json()


if __name__ == "__main__":
    print(historical_prices("EDP.LS", start="2021-01-19", end="2021-01-22"))
