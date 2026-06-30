class Solution:
    def isAnagram(self, s:str, t:str)->bool:
        if len(s) != len(t):
            return False
        counts = [0]*26
        for idx,char in enumerate(s):
            print(char)
            counts[ord(char)-ord('a')]+=1
            counts[ord(t[idx])-ord('a')]-=1
        for items in counts:
            if items != 0:
                return False
        return True