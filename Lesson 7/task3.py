from functools import wraps


def carry(func):
    args = []
    @wraps(func)
    def inner(n):
        args.append(n)
        if func.__code__.co_argcount == len(args):
            return func(*args)
        return inner
    return inner


@carry
def foo(a, b):
    return a + b


if __name__ == "__main__":
    print(foo(1)(5))

