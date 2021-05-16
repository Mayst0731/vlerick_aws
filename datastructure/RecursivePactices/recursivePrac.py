def rev(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + rev(s[:-1])


print(rev('hello world'))
print(rev('12345 6789'))