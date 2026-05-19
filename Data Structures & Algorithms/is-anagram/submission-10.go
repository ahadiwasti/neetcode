func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}
	counts := [26]int{}

	for idx, val := range s {
		counts[val-'a'] +=1
		counts[rune(t[idx]-'a')]-=1
	}
	for _,count := range counts {
		if count != 0 {
			return false
		}
	}
	return true
}
