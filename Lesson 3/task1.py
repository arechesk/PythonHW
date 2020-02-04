def squares(*args):
    return [i**2 for i in args]


def even_items(*args):
    return args[::2]


def cubes(*args):
    return [i**3 for i in filter(lambda x: x % 2 == 0, args[1::2])]

