func findMaxConsecutiveOnes(nums []int) int {
	count, max := 0, 0
	for _, n := range nums {
		if n == 1 {
			count++
		}else{
			count = 0
		}
		if count > max {
			max = count
		}
	}
	return max
}
