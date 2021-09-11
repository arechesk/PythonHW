# task 1
def capitalize(s: str):
    return " ".join([i.capitalize() for i in s.split(" ")])
# task 2

#%%
def character_counter(s: str):
    import collections
    c = collections.Counter()
    for i in s:
        c[i] += 1
    return dict(c)

# task 3


def my_trim(s: str):
    if len(s) < 2:
        return ""
    else:
        return s[:2]+s[-2:]
# task 4


def string_filter(lst: list):
    return len(
                list(
                    filter(
                        lambda i: len(i) >= 2 and i[0] == i[-1], lst)))
# task 5


def check_set(a: set, b: set, c: set):
    return c.issubset(a) and c.issubset(b)
# task 6


def square_generator(n: int):
    d = {i: i**2 for i in range(1, n+1)}
    print(d)
    return d
# task 7


def dict_merge(a: dict, b: dict):
    return a.copy().update(b)
# task 8


def find_heighest(d: dict):
    return sorted(d.values())[-3:][::-1]
# task 9


def my_uniq(lst: list):
    return list(set(lst))
# task 10


def diff_list(a: list, b: list):
    return list(set(a)-set(b))
