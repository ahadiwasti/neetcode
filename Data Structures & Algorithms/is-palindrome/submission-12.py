class Solution:
    def isPalindrome(self, s: str) -> bool:
        def valid(char):
            return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z') or ord('0') <= ord(char) <= ord('9')

        l,r = 0, len(s)-1

        while l<r:
            if not valid(s[l]):
                l+=1
                continue
            if not valid(s[r]):
                r-=1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1

        return True