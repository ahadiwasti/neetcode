func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}
	seen := make(map[rune]int)
	for _, val := range s {
		seen[val] +=1
	}
	for _,val := range t {
		if count,ok := seen[val];ok{
			if count > 0 {
				seen[val] -=1
			}else{
				return false
			}
		}else{
			return false
		}
	}

	
	return true
}
