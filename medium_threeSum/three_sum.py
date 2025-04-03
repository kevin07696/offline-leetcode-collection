from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    target = 0

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1
        while left < right:
            sum = a + nums[left] + nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

    return res
