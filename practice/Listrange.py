L = list(range(1, 11))
print('L=', L)

M = [x * x for x in range(1, 11)]
print('M=', M)

N = [x * x for x in range(1, 11) if x % 2 == 0]
print('N=', N)

L2 = ['Hello', 'World', 'Apple', 'None']
Q = [x.lower() for x in L2]
print('Q=', Q)
print(isinstance(None, str))

L1 = ['Hello', 'World', 18, 'Apple', None]
print("L1=", L1)
lenth = len(L1)
print('lenth_L1=', lenth)
L2 = []
i = 0
while i < lenth:
    if isinstance(L1[i], str):  # 先判断是否是str
        L2.append(L1[i].lower())
    else:
        L2 = L2   # 给L2赋值时同时剔除了不是str的
    i = i + 1  # 无论何种情况都要循环
print("L2=", L2)
