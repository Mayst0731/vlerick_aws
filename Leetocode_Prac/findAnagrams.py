def findAnagrams(s, p):
    result = []
    check_set = dict()

    for i in range(len(p)):
        if p[i] in check_set:
            check_set[p[i]] += 1

        else:
            check_set.update({p[i]: 1})

    for i in range(len(s) - len(p)+1):
        cur_set = dict()
        for j in range(i, i+len(p)):
            if s[j] in cur_set:
                cur_set[s[i]] += 1

            else:
                cur_set.update({s[j]: 1})

        if check_set.items() == cur_set.items():
            result.append(i)
        else:
            continue

    return result


print(findAnagrams("abab","ab"))