func productExceptSelf(nums []int) []int {
	ans := make([]int,len(nums))
	prefix := 1
	for i:=0;i<len(nums);i++{
		ans[i] = prefix
		prefix *= nums[i]
	}
	postfix := 1
	for j:=len(nums)-1;j>=0;j--{
		ans[j] *= postfix
		postfix *= nums[j]
	}
	return ans

}
