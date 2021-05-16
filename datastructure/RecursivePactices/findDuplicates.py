def find_repeat(nums):
    # Find a number that appears more than once

    for needle in range(0, len(nums)):

        for check in range(needle + 1, len(nums)):

            if nums[needle] == nums[check]:
                return nums[needle]

    return -1