func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}
	counts := make(map[rune]int)
	countt := make(map[rune]int)

	for idx, val := range s {
		counts[val] +=1
		countt[rune(t[idx])] +=1
	}
	for val,count := range counts {
		if countt[val] != count{
			return false
		} 
	}
	return true
}
