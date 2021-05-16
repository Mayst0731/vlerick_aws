def removeDuplicates(nums):
    check_point = 1
    sit_point = 0

    while check_point < len(nums):
        if nums[check_point] != nums[check_point - 1]:
            nums[sit_point] = nums[check_point]
            sit_point += 1
            check_point += 1
        elif check_point == len(nums):
            nums[sit_point] = nums[check_point]
        else:
            check_point += 1

    return nums

print([1,1,2])
print(removeDuplicates([1,1,2]))