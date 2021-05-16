d={'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

for ch in 'efg':
    print(ch)

from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['a', 'b', 'c']):       #  enumerate() 可以将list变成类似dict的
    print(i, value)

for x,y in[(1,1), (2,4), (3,9)]:
    print(x,y)