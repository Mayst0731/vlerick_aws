def search(nums, target) -> int:
    start = 0

    end = len(nums) - 1

    while start < end:

        mid = start + (end - start) // 2

        if nums[mid] == target:

            return mid

        elif nums[mid] < target:

            start = mid + 1
        else:

            end = mid - 1

    return -1

print(search([5],5))