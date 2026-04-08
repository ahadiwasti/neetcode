func removeElement(nums []int, val int) int {
    temp := []int{}
	for _, n := range nums {
		if n != val {
			temp = append(temp, n)
		}
	}
	for i := 0; i <len(temp); i++{
		nums[i] = temp[i]
	}
	
	return len(temp)
}
