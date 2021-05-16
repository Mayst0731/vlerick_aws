# strings = ('a', 'b', 'a', 'a',
#            'c', 'a', 'b', 'a')
# counts = {}
#
# for kw in strings:
#     if kw not in counts:
#         counts[kw] = 1
#     else:
#         counts[kw] += 1
#
# print(counts)
from collections import defaultdict
def zero():
    return 0

a = defaultdict(zero)

# print('before add new value, a:',a)
#
# print(a['you'])

print('after add new value, a:', a)
strings = ('a', 'b', 'a', 'a',
           'c', 'a', 'b', 'a')
counts = defaultdict(lambda: 0)  # use lambda to simply define a function

for s in strings:
    counts[s] += 1

print(counts)