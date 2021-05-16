
def searchInsert(nums, target) -> int:

    start = 0

    end = len(nums) - 1

    if target > nums[end]:

        return len(nums)

    elif target <= nums[start]:

        return 0

    while start <= end:

        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            if target > nums[mid - 1]:
                return mid
            else:
                end = mid

        else:
            if target < nums[mid + 1]:
                return mid + 1
            else:
                start = mid + 1


# print(searchInsert([1,3,5,6],5))
# print(searchInsert([1,3,5,6], 2))
# print(searchInsert([1,3,5,6],7))
# print(searchInsert([1,3,5,6], 0))
print(searchInsert([1], 1))






