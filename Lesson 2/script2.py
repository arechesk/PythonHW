# task 1


def print_interval(x: int):
    result = []
    for i in range(0, x+1):
        if not i % 2:
            continue
        else:
            result.append(i**2)
    print("squares: {}".format(" ".join([str(s) for s in result])))
    print("number of items: {}".format(len(result)))

# task 2


def check_div(a,b,c):
    counter =0
    for i in range(a+1,b):
        if not i % c:
            counter += 1
    return counter
# task 3


def factorial(n: int):
    result = 1
    if not n == 0:
        for i in range(1, n+1):
            result *= i
    return result


# task 4


def my_range(end, begin=0, step=1):
    result = []
    if begin == 0:
        i = 0
        while i < end:
            result.append(i)
            i += step
    else:
        i = end
        while i < begin:
            result.append(i)
            i += step
    return result
# task 5


def check_password(my_pass: str):
    while True:
        name = input("Please enter your name:")
        password = input("Please enter password:")
        if password == my_pass:
            print("Password for user: {0} is correct".format(name))
            break
        print("Password for user: {0} is incorrect".format(name))
        print("Please try again...")
