# python 3.5.2

import time
from functools import wraps


def required_natural_number(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        k = args[0]
        if isinstance(k, bool):
            raise TypeError
        if not isinstance(k, int) or k < 1:
            raise TypeError
        return func(*args, **kwargs)
    return wrapper


def _f(k):
    if k == 1 or k == 2:
        return 1
    else:
        return _f(k-1) + _f(k-2)


def _sum(k):
    if k == 1:
        return 1
    else:
        return k + _sum(k-1)


@required_natural_number
def fibonacci(k):
    return _f(k)


@required_natural_number
def sum_all(k):
    return _sum(k)


@required_natural_number
def delta_of_sum_all_and_fibonacci(k):
    x = sum_all(k) - fibonacci(k)
    return x if x >= 0 else -x


@required_natural_number
def surplus_time_by(k):
    return int(time.time() % k)
