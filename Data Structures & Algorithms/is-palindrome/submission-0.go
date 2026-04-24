func isPalindrome(s string) bool {
 start,end:=0,len(s)-1
 for start < end {
	for start < end && !isAlphanum(rune(s[start])){
		start += 1
	}
	for end > start && !isAlphanum(rune(s[end])){
		end -=1
	}
	if unicode.ToLower(rune(s[start])) != unicode.ToLower(rune(s[end])){
		return false
	}
	start += 1
	end -= 1
 }
 return true
}

func isAlphanum(c rune)bool{
	return unicode.IsLetter(c) || unicode.IsDigit(c)
}
