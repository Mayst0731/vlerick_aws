def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    #         set the point to check if exist repeat and i changed
    max_length = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                if j == len(s) - 1:
                    max_length = max(max_length, j - i + 1)
                else:
                    length = j - i + 1
                    max_length = max(max_length, j - i + 1)
            else:
                max_length = max(max_length, j - i)
                break
    return max_length

print("aabaa:", lengthOfLongestSubstring("aabaa"))
print("aab:", lengthOfLongestSubstring("aabaa"))
