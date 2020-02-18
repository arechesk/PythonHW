from functools import wraps
from time import time, sleep


def average_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"Среднее время работы {func.__name__}: {(time()-start)*1000:.0f} мс.")
        return result
    return inner


def time_methods(*args):

    def inner(cls):
        for i in args:
            try:
                func = getattr(cls, i)
                setattr(cls, i, average_time(func))
            except AttributeError:
                print(f"type object '{cls.__name__}' has no attribute '{i}'")
        return cls
    return inner


@time_methods('inspect', 'finalize')
class Spam:
    def __init__(self, s):
        self.s = s

    def inspect(self):
        sleep(self.s)

    def foo(self):
        return self.s


if __name__ == "__main__":
    a = Spam(2)
    a.inspect()
    a.foo()
