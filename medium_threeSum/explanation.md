# [Three Sum](https://neetcode.io/problems/three-integer-sum)

## Problem Statement
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
- The output should not contain any duplicate triplets. 
- You may return the output and the triplets in any order.

## 2 Pointer Solution
```python
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
                while nums[left] == nums[left-1] and left < right:
                    left += 1 
    
    return res
```

## How It Works

### Implementing 2 Pointers Algorithm
```python
nums.sort()
```

To use 2 pointers algorithm you need to sort the array first. 
If sum is greater than 0 you can decrement the largest element.
If sum is less than 0 you can increment the smallest element.
```python
while left < right:
    sum = a + nums[left] + nums[right]
    if sum > target:
        right -= 1
    elif sum < target:
        left += 1
```

### Handle Duplicates

We can start by checking that the previous element is not the same as the current element.
```python
if i > 0 and a == nums[i-1]:
    continue
```

In the inner loop we can decrement right and check that left iterator does not remain the same:
```python
left += 1
right -= 1
while nums[left] == nums[left-1] and left < right:
    left += 1 
while nums[right] == nums[right+1] and left < right:
    right -= 1 
```

## Example Walkthroughs

### Example 1: Handling Left Duplicates

```
1. nums = [0, 0, -1, 1] → sorted → [-1, 0, 0, 1]
2. a=-1 | l=0 | r=1 → sum=0 → res=[[-1, 0, 1]]
3. l=0 → r=0 → pointers meet
4. a=0 | l=0 | r=1 → sum=1 → right--
5. a=0 → a==nums[a-1] → skip duplicate
6. Final return: [[-1, 0, 1]]
```

### Example 2: Handling Internal Left Skipping

After finding a sum == 0, since nums[i] remains the same you need to make sure left and right values are different to make a unique triplet.
```
1. Sorted nums: [-1, 0, 0, 0, 1]
2. i=0 (a=-1):
   - left=1 (0), right=4 (1) → sum=0 → res=[[-1, 0, 1]]
   - left→2 (0), right→3 (0)
     [SKIP LEFT] nums[left]==nums[left-1] → left→3 (0)
     [SKIP RIGHT] nums[right]==nums[right+1] → right→2 (0)
   - left=3, right=2 → exit
3. i=1 (a=0):
   - left=2 (0), right=4 (1) → sum=1 → right→3 (0)
   - sum=0 → res=[[-1,0,1], [0,0,0]]
   - left→3 (0), right→2
     [SKIP LEFT] nums[left]==nums[left-1] → left→4
     [SKIP RIGHT] (right+1=3 is out of bounds)
   - left=4, right=2 → exit
4. i=2 (a=0):
   - [SKIPPED] a==nums[i-1]
5. Final result: [[-1, 0, 1], [0, 0, 0]]
```

## Complexity Analysis
- **Time:** O(n^2) where sort: O(n log n) + outer: O(n) * inner: O(n)
- **Space:** O(1) only stores left and right pointers




