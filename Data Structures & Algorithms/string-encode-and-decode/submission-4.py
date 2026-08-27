class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        r = 0
        while r < len(s):
            l = r
            while s[r] != '#':
                r+=1
            wlen = int(s[l:r])
            l=r+1
            r=l+wlen
            res.append(s[l:r])
        return res
