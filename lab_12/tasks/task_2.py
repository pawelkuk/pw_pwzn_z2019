from datetime import datetime
from functools import wraps
from time import time


def log_run(fun):
    def wrapper(*args, **kwargs):
        start = time()
        print(f"{datetime.now()}| function{ fun.__name__ } called with:")
        print(f"{len(args)} positional parameters")
        print(f'optional parameters: {kwargs.keys() if len(kwargs) else "-"}')
        res = fun(*args, **kwargs)
        print(f"returned: {res} ({time() - start:+.2e})")

    return wrapper


@log_run
def fun(*args, **kwargs):
    pass


if __name__ == "__main__":
    decorated_sum = log_run(sum)
    decorated_sum([1, 2, 3])
    fun(1, 2, "a", bb=1)
    # Przykładowy log
    # 2020-01-23T21:09:55| function sum called with:
    # 1 positional parameters
    # optional parameters: -
    # returned: 6 (1.43e-06s)
    # 2020-01-23T21:09:55| function fun called with:
    # 3 positional parameters
    # optional parameters: bb
    # returned: None (1.43e-06s)
