func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
    for idx,val := range nums{
       if res,ok := seen[target-val];ok{
        return []int{res,idx}
       }
       seen[val] = idx
    }
    return nil
}
