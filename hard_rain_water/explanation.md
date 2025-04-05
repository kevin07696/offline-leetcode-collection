# [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

![rainwatertrap](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

## 2 Pointers Solution
```python
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
```

## How It Works

### Calculating Trapped Water
```
Water at current position = min(leftMax, rightMax) - currentHeight
```

- `leftMax`: The highest bar encountered so far from the left side
- `rightMax`: The highest bar encountered so far from the right side
- The minimum of these two maxima determines the water level at the current position
- Subtract the current height to get the water trapped at that position

### Implementing 2 Pointers Algorithm
```python
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
```

- Use left and right pointers starting at both ends
- The smaller of `height[left]` and `height[right]` determines which pointer to move
- Update the respective max when a new higher bar is found
- Add trapped water when current height is below the current max

## Example Walkthroughs

### Example 1:
```
[0,1,0,2,1,0,1,3,2,1,2,1]

Initial: left=0, right=11, leftMax=0, rightMax=0, water=0

1. height[0]=0 < height[11]=1
   leftMax=0, so update leftMax=0
   water += 0-0 = 0
   left=1

2. height[1]=1 > height[11]=1
   rightMax=0, so update rightMax=1
   right=10

3. height[1]=1 < height[10]=2
   leftMax=0 < height[1]=1, update leftMax=1
   left=2

4. height[2]=0 < height[10]=2
   leftMax=1 > height[2]=0
   water += 1-0 = 1
   left=3

... (continuing similarly)

Final water = 6
```

### Example 2:
Edge-case: all bars same height
```
[2,2,2,2]

All steps will only update leftMax/rightMax but never add water
Final water = 0
```

### Example 3:
Edge-case: descending then ascending
```
[4,2,0,3,2,5]

1. Left side dominates until right pointer finds taller bar
2. Right side then dominates and captures trapped water
Final water = 9
```

## Complexity Analysis
- **Time:** O(n): Each element is visited exactly once by either left or right pointer
- **Space:** O(1): Only uses constant space for pointers and max variables

## Key Insight
The solution efficiently calculates trapped water by recognizing that the water level at any point is determined by the lower of the highest bars on either side, and processes the array from both ends inward to find these maxima.