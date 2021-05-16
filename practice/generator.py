from collections import Iterable, Iterator

g = (x * x for x in range(11))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(5)
print(f)
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 将可迭代的变成迭代器
print(isinstance(iter([]), Iterator))
print(isinstance(iter({})), Iterator)

# Iterator 可以表示一个无限大的数据流，例如全体自然数，但list是永远不可能存储全体自然数的
# 凡事可作用于for循环的对象都是 Iterable 类型
# 凡事可作用于 next（）函数的对象都是iterable 类型， 他们表示一个惰性计算的序列
# 集合数据类型 list、 dict、 str等是iterable 但不是iterator，可以用iter()函数获得interator对象
