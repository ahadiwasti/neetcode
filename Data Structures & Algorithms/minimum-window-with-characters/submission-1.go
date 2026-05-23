func minWindow(s string, t string) string {
    if t == "" {
		return ""
	}
	res:=[]int{-1,-1}
	reslen:=math.MaxInt32
	l:=0
	window:=make(map[rune]int)
	countT:=make(map[rune]int)
	for _,countt:= range t{
		countT[countt]++
	}
	have,need:=0,len(countT)
	for r:=0;r<len(s);r++{
		c:= rune(s[r])
		window[c]++
		if countT[c] >0 && countT[c] == window[c]{
			have++
		}
		for need == have {
			if (r-l+1) < reslen{
				reslen = r-l+1
				res=[]int{l,r}
			}
			window[rune(s[l])]--
			if countT[rune(s[l])] >0 && window[rune(s[l])] < countT[rune(s[l])]{
				have--
			}
			l++
		}
	}
	if res[0] == -1{
		return ""
	}
	return s[res[0]:res[1]+1]
}
