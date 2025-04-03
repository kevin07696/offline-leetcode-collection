package regexhard

func IsMatch(s string, p string) bool {

	cache := map[[2]int]bool{}
	
	var dfs func(int, int) bool
	dfs = func (i, j int) bool {
		key := [2]int{i, j}

		if cached, ok := cache[key]; ok {
			return cached
		}
		
		if i >= len(s) && j >= len(p) {
			return true
		}

		if j >= len(p) {
			return false
		}

		match := i < len(s) && j < len(p) && (s[i] == p[j] || p[j] == '.')
		
		if j+1 < len(p) && p[j+1] == '*' {
			cache[key] = dfs(i, j+2) || (match && dfs(i+1, j))

			return cache[key]
		}

		if match {
			cache[key] = dfs(i+1, j+1)

			return cache[key]
		}

		cache[key] = false
		return cache[key]
	}

	return dfs(0,0)
}
