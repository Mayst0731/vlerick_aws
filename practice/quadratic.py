import math


def quadratic(a, b, c):
    d = (b*b)-(4*a*c)
    if d < 0:
        print('no root')
    elif d == 0:
        root=(-b)/(2*a)
        return root
    else:
        d = math.sqrt(d)
        root1 = (-b+d)/(2*a)
        root2 = (-b-d)/(2*a)
        jie = [root1, root2]
        return jie


print('quadratic(2,3,1)=', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(1, 3, -4) == [1.0, -4.0]:
    print('测试成功')
else:
    print('测试失败')






