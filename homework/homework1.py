# Q Q3: Largest Factor
def largest_factor(n):
    u = 1
    q = []
    while (u < n):
        if n % u == 0:
            q.append(u)
            u += 1
        else:
            u += 1

    m = max(q)
    if m == 1:
        print(n, 'has no largest factor ')

    else:
        print(n, "'s largest factor is", m)
    return None


largest_factor(100)
largest_factor(97)
largest_factor(50)
largest_factor(17)
largest_factor(30)


def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    if c():
        return t()
    else:
        return f()


def with_if_function():
    return if_function(c(), t(), f())


def c():
    return False


def t():
    print(1)
    return None


def f():
    print(2)
    return None


with_if_statement()
result1 = with_if_statement()
print(result1)

with_if_function()

print(print(1), print(2))



