func groupAnagrams(strs []string) [][]string {
 //Sorting
	res := make(map[string][]string)
	for _, st := range strs {
		sorted := sortstring(st)
		res[sorted] = append(res[sorted], st)
	}
	var resp [][]string
	for _, val := range res{
		resp = append(resp, val)
	}
	return resp
}
func sortstring(st string) string{
	bytestr := []rune(st)
	sort.Slice(bytestr, func(i, j int) bool{
		return bytestr[i] < bytestr[j]
	})
	return string(bytestr)
}
