def longestPalindrome(s):
    visited = dict()
    valid_count = 0
    odd_number = 0
    for item in s:
        if item not in visited:
            visited[item] = 1
        else:
            visited[item] += 1

    for key, val in visited.items():
        if visited[key] % 2 == 0:
            valid_count += val
        else:
            valid_count += val - 1
            odd_number += 1

    if odd_number != 0:
        return valid_count + 1
    return valid_count

print(longestPalindrome('abccccdd'))