L = ['M', 'S', 'B', 'T', 'J']
print(L[0], L[1], L[2]) # M S B
print(L[0:3])  # M S B
print(L[1:3])  # S B 不含有最后一个
print(L[1:4])  # S B T
print(L[-1:])  # J  倒一的位置
print(L[-2:])  # T J  倒二的位置       正数和倒数的位置下角标数法不同，倒着从-1开始，正着就从0开始
print(L[-3:])  # B T J 倒三的位置
print(L[-2:-1])  # T 从首位置到尾位置，但不要尾位置
print(L[1:])  # 从第二个位置一直到结束
print(L[0:])
print(L[:1])  # 不要最右的
print(L[:2])
print(L[-10:])  # 取后十个数
print(L[:10])  # 取前十个数
M = 'ABCDEFG'
print(M[:3])  # A B C
