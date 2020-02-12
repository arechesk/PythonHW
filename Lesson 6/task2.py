
def get_public_attr(obj):
    return [i for i in dir(obj) if not i.startswith("__")]


if __name__ == "__main__":
    print(get_public_attr([]))
    print(get_public_attr(""))

