def cycle(obj):
    it = iter(obj)

    while True:
        try:
            yield next(it)
        except StopIteration:
            it = iter(obj)
            yield next(it)


if __name__ == "__main__":
    [print(i) for i in cycle([1, 2, 3])]


