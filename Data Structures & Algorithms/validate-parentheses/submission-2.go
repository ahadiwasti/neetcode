func isValid(s string) bool {
    slice := make([]byte,0,len(s))
	closetoopen := map[byte]byte{')':'(',']':'[','}':'{'}
	for _, cl := range s {
		if op, ok := closetoopen[byte(cl)];ok{
			if len(slice) == 0 {
				return false
			}
				top := slice[len(slice)-1]
				slice = slice[:len(slice)-1]
				if  top != op{
					return false
				}
		}else{
			slice = append(slice,byte(cl))
		}
	}
	return len(slice) == 0
}
