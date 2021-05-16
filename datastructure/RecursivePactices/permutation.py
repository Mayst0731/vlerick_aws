def permute(s):
    out = []
    # Base case
    if len(s) == 1:
        out = [s]
    # Recursive
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i]+s[i+1:]):
                print('previous out is', out)
                print('let is', let)
                print('perm is', perm)
                print('let + perm is ', [let + perm])
                out += [let+perm]
                print('current out is', out)
    return out


print(permute('abc'))

















































