def calc(numbers):
    s = 0
    for n in numbers:
        s = s+n*n
    return s

    a = calc([1, 2, 3])
    print(a)
    b = calc((4, 5, 6))
    print(b)