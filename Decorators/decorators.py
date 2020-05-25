from functools import wraps
from datetime import date
import time

# Template
def decorator(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapper_decorator


def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()

        value = func(*args, **kwargs)

        end = time.perf_counter()
        runtime = end - start

        # `!r` - convert the value to a string using repr()
        print(
            f"\U000023F0 The \033[1m{func.__name__!r}\033[0m function finished in \033[1m{runtime:.4f}\033[0m seconds."
        )

        return value

    return wrapper_timer


# Decorated function
@timer
def now():
    today = date.today().strftime("%d/%m/%Y")
    print(f"Date: {today}")


now()
