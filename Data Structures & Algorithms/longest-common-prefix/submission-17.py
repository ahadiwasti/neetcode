class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]

        for i in range(len(base)):
            for char in strs[1:]:
                if i >= len(char) or char[i] != base[i]:
                    return base[:i]

        return base