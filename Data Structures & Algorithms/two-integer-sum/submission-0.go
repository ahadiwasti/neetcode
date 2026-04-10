func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
	for i,num := range nums {
		if res , ok := seen[target-num]; ok{
			return []int{res, i}
		}else{
			seen[num] = i
		}
	}
	return nil
}
