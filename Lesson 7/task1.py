from functools import wraps
from time import time, sleep


def average_time(func=None, *, n=2):
    if func is None:
        return lambda f: average_time(f, n=n)
    cache = []
    @wraps(func)
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        cache.append(time()-start)
        print(f"Среднее время работы: {sum(cache)/len(cache)*1000:.0f} мс.")
        return result
    return inner


@average_time(n=2)
def foo(a):
    sleep(a)
    return a


if __name__ == "__main__":
    print(foo(3))
    print(foo(7))
    print(foo(1))
