class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]


        for i in range(len(base)):
            for s in strs:
                if i > len(s)-1 or s[i] != base[i]:
                    return base[:i]

        return base