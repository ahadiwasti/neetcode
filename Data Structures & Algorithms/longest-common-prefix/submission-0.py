class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]

        for i in range(1,len(strs)):
            j = 0
            while j < min(len(strs[i]), len(base)):
                if base[j] != strs[i][j]:
                    break
                j+=1
            base = base[:j]

        return base
                