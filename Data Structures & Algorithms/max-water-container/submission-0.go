func maxArea(heights []int) int {
	maxarea:=0
	i,j:=0,len(heights)-1
	for i<j{
		area := (j-i)*min(heights[i],heights[j])
		if area > maxarea{
			maxarea = area
		}
		if heights[i]<= heights[j]{
			i++
		}else{
			j--
		}
	}
	return maxarea
}

func min(a,b int) int{
	if a<b{
		return a
	}
	return b
}