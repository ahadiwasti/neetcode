class Solution:
    def isAnagram(self, s:str, t:str)->bool:
        if len(s) != len(t):
            return False

        freq = [0]*26

        for idx in range(len(s)):
            freq[ord(s[idx])-ord('a')]+=1
            freq[ord(t[idx])-ord('a')]-=1

        for count in freq:
            if count > 0:
                return False

        return True