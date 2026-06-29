func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}

    countS := [26]int{}

    for idx, s := range s {
        countS[s-'a']++
        countS[rune(t[idx])-'a']--
    }
    for _,counts := range countS{
        if counts != 0{
            return false
        }
    }

    return true

}