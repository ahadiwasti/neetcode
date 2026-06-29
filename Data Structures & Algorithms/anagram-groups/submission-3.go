func groupAnagrams(strs []string) [][]string {
 //Hashmap
resgroup := make(map[[26]int][]string)
for _,val := range strs{
    count := [26]int{}
    for _, char := range val{
        count[char-'a']++
    }

    resgroup[count] = append(resgroup[count], val)
}

res := [][]string{}

for _, groups := range resgroup{
    res = append(res,groups)
}
return res

}
