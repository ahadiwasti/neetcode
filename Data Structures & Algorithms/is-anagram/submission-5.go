func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}
	s1 := make(map[rune]int)
	t1 := make(map[rune]int)
	for i := 0; i <len(s) ; i++{
		s1[rune(s[i])]++
		t1[rune(t[i])]++
	}
	for _, val := range s {
		if s1[val] != t1[val]{
			return false
		}
	}
	return true
}
