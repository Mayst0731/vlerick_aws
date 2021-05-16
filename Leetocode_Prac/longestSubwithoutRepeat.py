def lengthOfLongestSubstring(s):

    def hasduplicate(s):
        has_duplicate = False
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    has_duplicate = True
                    break

            if has_duplicate == True:
                break

        return has_duplicate

    if len(s) <= 1:
        return len(s)

    sub_string = []
    max_length = 0

    for i in range(len(s)-1):
        for j in range(i, len(s)):
            sub_string.append(s[i:j+1])

    for sub in sub_string:
        if hasduplicate(sub) == False:
            length = len(sub)
            max_length = max(max_length, length)

    return max_length


print(lengthOfLongestSubstring("abcbauiafajl"))
