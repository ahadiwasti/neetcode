class Solution:
    def isAnagram(self, s:str, t:str)->bool:
        if len(s) != len(t):
            return False

        freq = [0]*26
        for i in range(len(s)):
            freq[ord('a')-ord(s[i])]+=1
            freq[ord('a')-ord(t[i])]-=1

        for count in freq:
            if count > 0:
                return False

        return True 
