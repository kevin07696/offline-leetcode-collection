from typing import List


def maxArea(heights: List[int]) -> int:
    max = 0
    l = 0
    r = len(heights)-1
    while l < r:
        a = r-l
        if heights[l] < heights[r]:
            a *= heights[l]
            l += 1
        else:
            a *= heights[r]
            r -= 1
        if a > max:
            max = a
    return max