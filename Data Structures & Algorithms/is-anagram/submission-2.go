func isAnagram(s string, t string) bool {
    if len(s) != len(t){
        return false
    }
     counts,countt := make(map[rune]int), make(map[rune]int)
    
     for i,val := range s {
        counts[val]++
        countt[rune(t[i])]++
     }
     for k,v := range counts {
        if countt[k] != v {
            return false
        }
     }
     return true
}
