def lengthOfLongestSubstring(s: str) -> int:
    start = -1
    max_len = 0
    d = {}

    for i in range(len(s)):
        if s[i] in d and start < d[s[i]]:
            start = d[s[i]]
            d[s[i]] = i
        else:
            d[s[i]] = i
            max_len = max(max_len, i - start)
    return max_len


print(lengthOfLongestSubstring("tmmzuxt"))



