class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for char in strs:
            res.append(str(len(char)))
            res.append('#')
            res.append(char)

        return ''.join(res)


    def decode(self,strs:str)-> List[str]:
        res = []
        j = 0
        while j < len(strs):
            i = j
            while strs[j] != '#':
                j+=1

            rlen = int(strs[i:j])
            i = j+1
            j = i+rlen
            st = strs[i:j]

            res.append(st)

        return res

