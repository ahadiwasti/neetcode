class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l = 0
        while l < len(word1) and l < len(word2):

            res.append(word1[l])
            res.append(word2[l])
            l+=1

        res.append(word1[l:] or word2[l:])
        return "".join(res)