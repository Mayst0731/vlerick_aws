def maxSubArray(nums):

    globalMax = currMax = nums[0]

    for i in range(1, len(nums)):

        currMax = max((currMax + nums[i]), nums[i])

        if currMax >= globalMax:
            globalMax = currMax

    return globalMax

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))