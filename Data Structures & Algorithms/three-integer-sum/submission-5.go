func threeSum(nums []int) [][]int {
res := [][]int{}
sort.Ints(nums)
for i:=0;i<len(nums)-2;i++{
	if nums[i]>0{
		break
	}
	if i > 0 && nums[i] == nums[i-1]{
		continue
	}
	l,r:=i+1,len(nums)-1
	for l<r{
		threesum:= nums[i]+nums[l]+nums[r]
		if threesum < 0 {
			l += 1
		}else if threesum > 0 {
			r -= 1
		}else{
			res = append(res,[]int{nums[i],nums[l],nums[r]})
			l++
			r--
			for l < r && nums[l] == nums[l-1]{
				l++
			}
			for r > l && nums[r] == nums[r+1]{
				r--
			}
		}
	}
}
return res
}
