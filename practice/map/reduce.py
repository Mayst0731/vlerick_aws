from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print('r=x*x:', list(r))

a = list(map(str, [1, 2, 3, 4, 5, 6, 7]))
print(a)


def add(x, y):
    return x + y


b = reduce(add, [1, 3, 5, 7])
print('b=', b)

L1 = ['adam', 'LISA', 'barT']


def normalize(s):
    return s.capitalize()


print(list(map(normalize, L1)))

L2 = [3,5,7,9]


def multiply(x, y):
    return x * y


def prod(L):
    return reduce(multiply, L)

print(prod(L2))


def str2float(s):
    def strInt(s):
        L = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,'9': 9,'0': 0, '.': '.'}
        return L[s]
    ints = list(map(strInt, s))
    print(ints)
    tenProduct = [ints[0] * 100, ints[1] * 10, ints[2]]
    negaProduct = [ints[4] * 0.1, ints[5] * 0.01, ints[6] * 0.001]
    tenProduct.extend(negaProduct)
    Product = reduce(add, tenProduct)
    return Product


print(str2float('123.456'))

