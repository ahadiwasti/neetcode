class Solution:
    def isPalindrome(self, s: str) -> bool:
        def valid(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
        left,right = 0,len(s)-1

        while left < right:
            while left < right and not valid(s[left]):
                left+=1
            while right > left and not valid(s[right]):
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True
             
