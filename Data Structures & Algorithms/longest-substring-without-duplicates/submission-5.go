func lengthOfLongestSubstring(s string) int {
seen:=make(map[byte]int)
l,longest:=0,0
for r:=0;r<len(s);r++{
	if idx,ok:= seen[s[r]];ok{
		l = max(idx+1,l)
	}
	seen[s[r]]= r
	if r-l+1 > longest{
		longest = r-l+1
	}
}
return longest
}
