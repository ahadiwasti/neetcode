func characterReplacement(s string, k int) int {
    count := make(map[byte]int)
	res,l,max:= 0,0,0
	for r:=0;r<len(s);r++{
		count[s[r]]++
		if count[s[r]] > max{
			max = count[s[r]]
		}
		for (r-l+1)-max > k {
			count[s[l]]--
			l++
		}
		if (r-l+1)>res{
			res = r-l+1
		}
	}
	return res
}