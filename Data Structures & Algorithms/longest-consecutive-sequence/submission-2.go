func longestConsecutive(nums []int) int {
longest := 0
hmp := make(map[int]struct{})
for _, num:= range nums {
	hmp[num] = struct{}{}
}

for _, num := range nums{
	if _, ok := hmp[num-1]; !ok{
		length := 1
		for {
			if _, exist := hmp[num+length]; exist{
				length += 1
			}else{
				break
			}
		}
		if length > longest {
			longest = length
		}
	}
}
return longest
}
