class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(char):
            return (ord('A') <= ord(char) <= ord('Z') or
            ord('a')<= ord(char)<= ord('z') or 
            ord('0')<= ord(char)<=ord('9'))

        left,right = 0,len(s)-1
        while left < right:
            while left < right and not helper(s[left]):
                left+=1
                continue
            while right > left and not helper(s[right]):
                right-=1
                continue

            if s[left].lower() != s[right].lower():
                return False
            
            left+=1
            right-=1
        return True