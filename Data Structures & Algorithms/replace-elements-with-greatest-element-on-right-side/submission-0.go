func replaceElements(arr []int) []int {
ans :=make([]int,len(arr))
maxN := -1
for i := len(arr)-1; i>= 0; i--{
	ans[i] = maxN
	if arr[i] > maxN{
		maxN = arr[i]
	}
}
return ans
}
