class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            res.append(word)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        right = 0

        while right < len(s):
            left = right
            while s[right] != "#":
                right +=1

            reslen = int(s[left:right])
            left = right+1
            right = left+reslen
            res.append(s[left:right])

        return res


