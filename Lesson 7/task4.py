from functools import wraps


def type_check(func):
    @wraps(func)
    def inner(*args, **kwargs):
        types = func.__annotations__.values()
        params = list(args) + list(kwargs.values())
        if len(types) != len(params):
            raise TypeError("Wrong annotation")
        for a, t in zip(params, types):
            if not isinstance(a, t):
                print(f"{a} is not {t}")
        func(*args, **kwargs)
        return inner
    return inner


@type_check
def f(a: int, b: int):
    return a+b


if __name__ == "__main__":
    f(1, 0.9)
