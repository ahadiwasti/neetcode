func groupAnagrams(strs []string) [][]string {
 //Hashmap
 resgroup := make(map[[26]int][]string)
 for _, values := range strs{
	var charcount [26]int
	for _, val := range values{
		charcount[val-'a']++
	}
	resgroup[charcount] = append(resgroup[charcount], values)
 }

 var resp [][]string

 for _, resg := range resgroup {
	resp = append(resp, resg)
 } 
 return resp
	
}
