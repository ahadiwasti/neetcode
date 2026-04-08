func calPoints(operations []string) int {
	record := []int{}
	score := 0
	for _, ops := range operations{
		le := len(record)
		if ops == "+"{
			record = append(record, record[le-1]+record[le-2])
			score += record[le]
		}else if ops == "D"{
			record = append(record, 2*record[le-1])
			score += record[le]
		}else if ops == "C" {
			score -= record[le-1]
			record = record[:le-1]
		}else {
			num,_ := strconv.Atoi(ops)
			record = append(record, num)
			score += num
		}
	} 
	return score
}
