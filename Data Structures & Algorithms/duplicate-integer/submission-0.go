func hasDuplicate(nums []int) bool {
    seen := make(map[int]int)

    for i,num := range nums{
        if _,ok := seen[num]; !ok{
            seen[num] = i 
        }else{
            return true
        }
    }
    return false
}
