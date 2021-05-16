def permute(nums):
    if len(nums) <= 1:
        return [nums]

    else:
        answer = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i + 1:]  # 除去num的n
            for y in permute(n):     # 遍历permute过的n
                answer.append([num] + y)

    return answer


print(permute(['1', '2', '3']))
