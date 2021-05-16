def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('jack', 30)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 30, city=extra['city'], job=extra['job'])
person('Jack', 30, **extra)


def person1(name, age, *, job, city='BJ'):
    print(name, age, job, city)


#所以不用考虑传入参数的顺序了,且city有默认值
person1('J', 24, job='engineer', city='BJ')
person1('J', 24, job='engineer')
