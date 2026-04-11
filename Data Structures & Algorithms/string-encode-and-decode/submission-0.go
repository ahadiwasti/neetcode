type Solution struct{}

func (s *Solution) Encode(strs []string) string {
 var encoded string
 for _, val := range strs {
	encoded += strconv.Itoa(len(val))+"#"+val
 }
 return encoded
}

func (s *Solution) Decode(encoded string) []string {
 decoded := []string{}
 i := 0
 for i < len(encoded){
	j := i
	for encoded[j] != '#' {
		j++
	}
	charlen,_ := strconv.Atoi(encoded[i:j])
	i = j+1
	decoded = append(decoded, encoded[i:charlen+i])
	i += charlen
 }
 return decoded
}