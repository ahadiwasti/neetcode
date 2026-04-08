func isValid(s string) bool {
    slice := []rune{}
	closetoopen := map[rune]rune{')':'(',']':'[','}':'{'}
	for _, cl := range s {
		if op, ok := closetoopen[cl];ok{
			if len(slice) == 0 {
				return false
			}
				top := slice[len(slice)-1]
				slice = slice[:len(slice)-1]
				if  top != op{
					return false
				}
		}else{
			slice = append(slice,cl)
		}
	}
	return len(slice) == 0
}
