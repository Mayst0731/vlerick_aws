def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'



def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5

o = odd()
next(o)
next(o)
next(o)
