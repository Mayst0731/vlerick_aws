def product(*x):
    p = 1
    for n in x:
       p = p*n
    return p


print('product(5)=', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

if product(5) != 5:
    print('测试失败！')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    print('测试成功!')
    #try:
     #   product()
      #  print('测试失败！')
    #except TypeError:
     #   print('测试成功!')

a=product()
print(a)