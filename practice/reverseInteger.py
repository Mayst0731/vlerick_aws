def reverse(x):

    validbound = 2 ** 31 - 1
    if x > validbound or x < 0 - 2 ** 31 or x == 0:
        return 0

    if x < 0:
        a = -x

    else:
        a = x

    num = 0

    while a != 0:
        temp = a % 10
        num = num * 10 + temp
        a = a // 10

    if x < 0:
        num = -num
        return num
    elif x > 0:
        return num

print(reverse(1534236469))