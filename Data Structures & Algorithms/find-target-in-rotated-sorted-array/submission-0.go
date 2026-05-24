func search(nums []int, target int) int {
	//trivial approach
	for idx,val:=range nums{
		if val == target{
			return idx
		}
	}
	return -1
}
