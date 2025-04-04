# [Container With Most Water](https://neetcode.io/problems/max-water-container)

## Problem Statement
You are given an integer array heights where heights[i] represents the height of the ith bar.
- You may choose any two bars to form a container.
- Return the maximum amount of water a container can store.

![bar-diagram](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/77f004c6-e773-4e63-7b99-a2309303c700/public "bar-diagram")

## 2 Pointers Solution
```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
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
```

## How It Works

### Calculating Area
```
Area = (xr-xl)*min(yr,yl)
```

- x-length = right index minus left index
- y-length = minimum height of the bar
- The minmum height between the bars will show how high the water can rise to without spillage.

### Implementing 2 Pointers Algorithm
```python
while l < r:
    a = r-l
    if heights[l] < heights[r]:
        a *= heights[l]
        l += 1
    else:
        a *= heights[r]
        r -= 1
```

- Use left-most and right-most pointers to get the maximum width of the water tank
- Whichever side has the shorter height you increment to find a taller height
- If it is equal it does not matter which side you increment from.


## Example Walkthroughs

### Example 1:
```
[1,7,2,5,4,7,3,6]

(xr-xl)*min(yr,yl) = area
1. (7-0)*min(6,1) = 7
    h1 < hr, thus l++
    
2. (7-1)*min(6,7) = 36
    h1 >= hr, thus r--

3. (6-1)*min(3,7) = 15
    hl >= hr, thus r--

4. (5-1)*min(7,7) = 28
    hl >= hr, thus r--

5. (4-1)*min(7,4) = 12
    hl >= hr, thus r--

6. (3-1)*min(7,5) = 10
    hl >= hr, thus r--

7. (2-1)*min(7,2) = 2
    hl >= hr, thus r--
    
loop ends when l == r
maximum area = 36
```

### Example 2:
Edge-case: all bars are the same height
```
[2,2,2]

(xr-xl)*min(yr,yl) = area
1. (2-0)*min(2,2) = 4
    hl >= hr, thus r--
2. (1-0)*min(2,2) = 2
    hl >= hr, thus r--

loop ends when l == r
maximum area = 4
```

### Example 3
Edge-case: the maximum area not using maximum bars
```
[1,1,4,4,1,1]
(xr-xl)*min(yr,yl) = area
1. (5-0)*min(1,1) = 5
    h1 >= hr, thus r--
2. (4-0)*min(1,1) = 4
    h1 >= hr, thus r--
3. (3-0)*min(4,1) = 3
    h1 < hr, thus l++
4. (3-1)*min(4,1) = 2
    h1 < hr, thus l++
5. (3-2)*min(4,4) = 4
    h1 >= hr, thus r--

loop ends when l == r
maximum area = 5
```

## Complexity Analysis
- **Time:** O(n): The worst case is when left and right are adjacent, they produces the largest area.  
- **Space:** O(1) The solution only stores left and right pointers and the area.

