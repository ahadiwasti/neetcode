class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(char):
            return ((ord('A')<= ord(char) <= ord('Z')) or 
            (ord('a')<=ord(char)<=ord('z')) or ord('0') <= ord(char)<=ord('9') )

        l,r = 0,len(s)-1

        while l < r:
            while l< r and not helper(s[l]):
                l+=1
                continue
            while r > l and not helper(s[r]):
                r-=1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1
        return True