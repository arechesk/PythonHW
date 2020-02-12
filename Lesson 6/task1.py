class EvenIterator(object):
    def __init__(self,collection):
        self.iter = iter(collection[::2])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)


if __name__=="__main__":
    for i in EvenIterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        print(i)


