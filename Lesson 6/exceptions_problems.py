# Enter your code here. Read input from STDIN. Print output to STDOUT
def check(i):
    try:
        i = int(i)
        return i
    except TypeError:
        print(f"Error Code: invalid literal for int() with base 10: \'{i}\'")
        raise TypeError()


def div(a, b):
    try:
        print(check(a) // check(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except TypeError:
        pass


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = input().split()
        div(a, b)


