# Regular Expression Matching

## Problem Statement
Given an input string (`s`) and a pattern (`p`), implement regular expression matching with support for:
- `.` Matches any single character
- `*` Matches zero or more of the preceding element

## Recursive Solution with Memoization (Decision Tree)
For patterns containing `*`, we use depth-first search with memoization:

```python
def isMatch(s: str, p: str) -> bool:
    memo = {}
    
    def dfs(i: int, j: int) -> bool:
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Base cases
        if j >= len(p):
            return i == len(s)
        
        match = i < len(s) and (p[j] == '.' or s[i] == p[j])
        
        # Handle '*' operator
        if j + 1 < len(p) and p[j+1] == '*':
            memo[(i, j)] = dfs(i, j+2) or (match and dfs(i+1, j))
            return memo[(i, j)]
        
        # Simple character match
        if match:
            memo[(i, j)] = dfs(i+1, j+1)
            return memo[(i, j)]
        
        return False
    
    return dfs(0, 0)
```

## How It Works

### Star (`*`) Operator Handling
```
if j + 1 < len(p) and p[j+1] == '*':
    return dfs(i, j+2) or (match and dfs(i+1, j))
```
- **Option 1 (skip `*`):** `dfs(i, j+2)` → ignore current pattern char and `*`
- **Option 2 (use `*`):** `match and dfs(i+1, j)` → consume current char if it matches

### Termination Conditions
1. **Full match:** `i == len(s)` and `j == len(p)` → `True`
2. **Pattern exhausted:** `j == len(p)` but `i < len(s)` → `False`
3. **No match:** Current characters don't match → `False`

## Example Walkthroughs

### Example 1: `s = "aaaa"`, `p = ".a*"`
Passes with the last pattern `a*` matching chars for `s[1:]`
```
dfs(0,0) = match && dfs(1, 1) -> true
match = true
dfs(1,1) =  dfs(1,3)  || (match && dfs(2,1)) -> true
dfs(1,3) = false
match = true
dfs(2,1) = dfs(2,3) || (match && dfs(3,1)) -> true
dfs(2,3) = false
match = true
dfs(3,1) = dfs(3,3) || (match && dfs(4,1)) -> true
dfs(3,3) = false
match = true
dfs(4,1) = dfs(4,3) || (match && dfs(5,1)) -> true
dfs(4,3) = true
match = false

Final: True
```

### Example 2: `s = "aaaab"`, `p = ".a*"`

Fails because pattern p finishes iterating before string s
```
dfs(0,0) = match && dfs(1, 1) -> false
match = true
dfs(1,1) =  dfs(1,3)  || (match && dfs(2,1)) -> false
dfs(1,3) = false
match = true
dfs(2,1) = dfs(2,3) || (match && dfs(3,1)) -> false
dfs(2,3) = false
match = true
dfs(3,1) = dfs(3,3) || (match && dfs(4,1)) -> false
dfs(3,3) = false
match = true
dfs(4,1) = dfs(4,3) || (match && dfs(5,1)) ->  false
dfs(4,3) = false
match = false
      
Final: False
```

### Example 3: `s = "aaa"`, `p="a*aa"`
This stacktrace shows the repeated calls for dfs
```
dfs(0,0) = dfs(0,2) || (match && dfs(1,0)) -> true
  dfs(0,2) = dfs(0,4) || (match && dfs(1,2)) -> false
    dfs(0,4) = false
    match = true
    dfs(1,2) = dfs(1,4) || (match && dfs(2,2)) -> false
      dfs(1,4) = false
      match = true
      dfs(2,2) = dfs(2,4) || (match && dfs(3,2)) -> true
        dfs(2,4) = false
        match = true
        dfs(3,2) = dfs(3,4) || (match && dfs(3,3)) -> false
          dfs(3,4) = false
          dfs(3,3) = false
  match = true
  dfs(1,0) = dfs(1,2) || (match && dfs(2,0)) -> false
    dfs(1,2) = dfs(1,4) || (match && dfs(2,2)) -> false  # DUPLICATE CALL
      dfs(1,4) = false
      match = true
      dfs(2,2) = dfs(2,4) || (match && dfs(3,2)) -> true  # DUPLICATE CALL
        dfs(2,4) = false
        match = true
        dfs(3,2) = dfs(3,4) || (match && dfs(3,3)) -> false
          dfs(3,4) = false
          dfs(3,3) = false
    match = true
    dfs(2,0) = dfs(2,2) || (match && dfs(3,0)) -> true  # DUPLICATE CALL
      dfs(2,2) = dfs(2,4) || (match && dfs(3,2)) -> true  # DUPLICATE CALL
        dfs(2,4) = false
        match = true
        dfs(3,2) = dfs(3,4) || (match && dfs(3,3)) -> false
          dfs(3,4) = false
          dfs(3,3) = false
      match = true
      dfs(3,0) = dfs(3,2) || (match && dfs(4,0)) -> false
        dfs(3,2) = dfs(3,4) || (match && dfs(3,3)) -> false  # DUPLICATE CALL
          dfs(3,4) = false
          dfs(3,3) = false
        match = false
```

With memoization you can reduce the call stack:

```
dfs(0,0) = dfs(0,2) || (match && dfs(1,0)) -> true
  dfs(0,2) = dfs(0,4) || (match && dfs(1,2)) -> false
    dfs(0,4) = false
    match = true
    dfs(1,2) = dfs(1,4) || (match && dfs(2,2)) -> false  # Computed and stored
      dfs(1,4) = false
      match = true
      dfs(2,2) = dfs(2,4) || (match && dfs(3,2)) -> true  # Computed and stored
        dfs(2,4) = false
        match = true
        dfs(3,2) = dfs(3,4) || (match && dfs(3,3)) -> false  # Computed and stored
          dfs(3,4) = false
          dfs(3,3) = false
  match = true
  dfs(1,0) = [memo(1,2)=false] || (match && dfs(2,0)) -> false  # Used cached dfs(1,2)
    match = true
    dfs(2,0) = [memo(2,2)=true] || (match && dfs(3,0)) -> true  # Used cached dfs(2,2)
      match = true
      dfs(3,0) = [memo(3,2)=false] || (match && dfs(4,0)) -> false  # Used cached dfs(3,2)
```

## Complexity Analysis
- **Time:** O(m×n) where m = len(s), n = len(p) (with memoization)
- **Space:** O(m×n) for memoization cache

---

This solution efficiently handles all cases using recursive DFS with memoization to avoid redundant calculations. The decision tree branches at each `*` operator, exploring both skipping and consuming options.