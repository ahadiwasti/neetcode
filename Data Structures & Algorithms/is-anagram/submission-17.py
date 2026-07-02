class Solution:
    def isAnagram(self, s:str, t:str)->bool:
        if len(s) != len(t):
            return False
        counts = [0]*26
        for id,char in enumerate(s):
            counts[ord(char)-ord('a')]+=1
            counts[ord(t[id])-ord('a')]-=1
        for count in counts:
            if count > 0:
                return False
        return True