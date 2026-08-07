class Solution:
    def climbStairs(self,n):
        one,two = 1,1
        for i in range(n-1):
            one,two = one+two,one

        return one