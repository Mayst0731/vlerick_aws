def permute(nums):

    if len(nums) <= 1:
        return [nums]

    answer = []

    for i, num in enumerate(nums):
        n = nums[:i] + nums[i+1:]
        for y in permute(n):
            answer.append([num] + y)
    return answer


print(permute([1,2,3]))


