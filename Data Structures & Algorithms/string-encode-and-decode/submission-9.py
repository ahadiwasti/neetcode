class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for char in strs:
            res.append(str(len(char)))
            res.append("#")
            res.append(char)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        r = 0

        while r < len(s):
            l = r

            while s[r] != "#":
                r+=1
            reslen = int(s[l:r])
            l = r+1
            r = l+reslen
            res.append(s[l:r])


        return res