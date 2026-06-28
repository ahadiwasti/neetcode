func groupAnagrams(strs []string) [][]string {
 //Hashmap
resgroup := make(map[[26]int][]string)
for _,val := range strs{
    freqcount := [26]int{}
    for _,valx := range val{
        freqcount[valx-'a']++
    }
    resgroup[freqcount] = append(resgroup[freqcount],val)
}
var res [][]string
for _,group := range resgroup {
    res = append(res,group)
}

return res

	
}
