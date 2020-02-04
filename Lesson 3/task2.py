from functools import reduce


def foo(*args, **kwargs):
    if len(args) == 1 and isinstance(args[0], (int, float)):
        return args[0], args[0]
    elif len(args) == 1 and args[0] == [] or args[0] == ():
        return 0, 0
    elif len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0]
    for i in filter(lambda x: isinstance(x, (list, tuple)), args):
        if i in i:
            return None
    result = [foo(i) for i in args]
    result.extend([foo(i) for i in kwargs.values()])
    if None in result:
        return None
    result = list(map(lambda x: x[0] == 0 and (1, x[1])or (x[0], x[1]), result))
    return reduce(lambda x, y: (x[0]*y[0], x[1]+y[1]), result)


# if __name__=="__main__":
#     print(foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []])))

