func productExceptSelf(nums []int) []int {
	prefix := make([]int,len(nums))
	suffix := make([]int,len(nums))
	ans := make([]int,len(nums))
	prefix[0], suffix[len(nums)-1] = 1, 1

	for i := 1;i<len(nums);i++{
		prefix[i] = prefix[i-1]*nums[i-1]
	}
	for j := len(nums)-2;j>=0;j--{
		suffix[j] = suffix[j+1]* nums[j+1]
	}
	for k := 0; k< len(nums); k++{
		ans[k] = suffix[k]*prefix[k]
	}
	return ans

}
