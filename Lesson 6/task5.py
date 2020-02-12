def chain(*args):
    for i in args:
        for j in i:
            yield j


if __name__=="__main__":
    print(list(chain([1, 2, 3], [4, 5, 6])))


