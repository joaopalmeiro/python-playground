import time
from datetime import date
from functools import wraps


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
            f"\n\U000023F0 The \033[1m{func.__name__!r}\033[0m function finished in \033[1m{runtime:.4f}\033[0m seconds."
        )

        return value

    return wrapper_timer


def debug_args(func):
    @wraps(func)
    def wrapper_debug_args(*args, **kwargs):
        args_r = [repr(a) for a in args]
        kwargs_r = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_r + kwargs_r)
        print(f"\U0001F919 \033[1m{func.__name__}\033[0m({signature})\n")

        value = func(*args, **kwargs)
        return value

    return wrapper_debug_args


# Decorated function
@timer
@debug_args
def now():
    time.sleep(2)
    today = date.today().strftime("%d/%m/%Y")
    print(f"Date: {today}")


now()
