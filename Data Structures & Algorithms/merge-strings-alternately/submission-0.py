class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1,s2 = 0,0
        res = []

        while s1 < len(word1) and s2 < len(word2):
            res.append(word1[s1])
            res.append(word2[s2])

            s1+=1
            s2+=1

        res.append(word1[s1:])
        res.append(word2[s2:])

        return "".join(res)