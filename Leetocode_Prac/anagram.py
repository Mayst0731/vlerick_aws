def findAnagrams(s: str, p: str):
    res = []
    pset = dict()


    for start in range(0, len(s) - len(p) + 1):
        pset.clear()
        for i in range(len(p)):
            if p[i] not in pset:
                pset[p[i]] = 1
            else:
                pset[p[i]] += 1
        for j in range(start, start + len(p)):
            if s[j] not in pset:
                break
            elif s[j] in pset:
                pset[s[j]] -= 1

        check = True
        for value in pset.values():
            if value != 0:
                check = False
        if check == True:
            res.append(start)
    return res


print(findAnagrams("cbaebabacd","abc"))
