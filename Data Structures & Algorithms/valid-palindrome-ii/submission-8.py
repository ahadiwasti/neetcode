class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l,r):
            while l<r:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l+=1
                    r-=1
            return True

        le,ri = 0,len(s)-1

        while le<ri:
            if s[le].lower() != s[ri].lower():
                return check(le+1,ri) or check(le,ri-1)
            else:
                le+=1
                ri-=1

        return True