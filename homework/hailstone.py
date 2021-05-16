# Q5
def N_2(n):
    n = n / 2
    print(n)
    return n


def N_1(n):
    n = n * 3 + 1
    print(n)
    return n


def hailstone(n):
    print(n)
    i = 0
    while (n > 1):
        if n % 2 == 0:
            n = N_2(n)
            i = i + 1
            if n == 1:
                return i + 1
                break

        else:
            n = N_1(n)
            i = i + 1
            if n == 1:
                return i + 1
                break


a = hailstone(10)
print("a=", a)
