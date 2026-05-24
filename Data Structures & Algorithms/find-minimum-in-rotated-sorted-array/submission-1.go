func findMin(nums []int) int {
	//naive solution

	min:=nums[0]
	for i:=1;i<len(nums);i++{
		if nums[i]<min{
			min=nums[i]
		}
	}
	return min
}