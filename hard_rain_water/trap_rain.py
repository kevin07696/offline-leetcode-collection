from typing import List


def trap(height: List[int]) -> int:
    left = leftMax = rightMax = water = 0
    right = len(height)-1

    while left < right:
        if height[left] < height[right]:
            if leftMax < height[left]:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if rightMax < height[right]:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1
    return water