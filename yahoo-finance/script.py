from historical_prices import get_dataset

if __name__ == "__main__":
    data = get_dataset("MSFT", start="2019-04-15", end="2019-04-17")

    print(data)
