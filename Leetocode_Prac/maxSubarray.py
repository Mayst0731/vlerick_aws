#cur        -2 , 1, -3, 4, -1, 2, 1, -5, 4
#cur_max    -2 , -1,-3, 4, 3,  5, 6, 1,  5
#global_max -2 , 1,  1, 4, 4,  5, 6, 6,  6



def maxSubArray(nums) -> int:
    max_sum = nums[0]
    global_sum = nums[0]
    for i in range(1, len(nums)):
        if max_sum < 0:
            max_sum = nums[i]
        else:
            max_sum = max(max_sum, max_sum + nums[i])
    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))