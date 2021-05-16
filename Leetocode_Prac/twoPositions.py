def searchRange(nums, target):
    if len(nums) == 0:
        return [-1, -1]

    if len(nums) == 1 and nums[0] == target:
        return [0, 0]

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            start = mid
            end = mid
            while ((start - 1) >= 0) and (nums[start - 1] == target):
                start -= 1
            while ((end + 1) < len(nums)) and (nums[end + 1] == target):
                end += 1
            return [start, end]

        elif nums[mid] < target:

            left = mid + 1

        else:

            right = mid - 1
    return [-1, -1]

print(searchRange([1,4],4))