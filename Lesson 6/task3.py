def make_dict(a,b):
    return dict(zip(a, [b[i] if i < len(b) else None for i in range(len(a))]))


if __name__ == "__main__":
    print(make_dict([1, 2, 3], [4, 5, 6]))
    print(make_dict([1, 2, 3, 4, 5, 6, 7], []))
    print(make_dict([1, 2], [3, 4, 5, 6]))


