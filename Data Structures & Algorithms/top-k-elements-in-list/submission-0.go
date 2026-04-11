
func topKFrequent(nums []int, k int) []int {
// bucket sort

count := make(map[int]int)
for _, num := range nums{
	count[num]++
}

freqcount := make([][]int,  len(nums)+1)
for val, countr := range count {
	freqcount[countr] = append(freqcount[countr],val)
}

res := []int{}
for i:= len(freqcount)-1; i>0; i--{
	for _,numb := range freqcount[i]{
		res = append(res,numb)
		if len(res) == k {
			return res
		}
	}
}
return res
}
