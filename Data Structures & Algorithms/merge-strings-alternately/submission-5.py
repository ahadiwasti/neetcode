class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        res = []
        while index < len(word1) and index < len(word2):
            res.append(word1[index])
            res.append(word2[index])
            index+=1
        res.append(word1[index:] or word2[index:])
        return "".join(res)