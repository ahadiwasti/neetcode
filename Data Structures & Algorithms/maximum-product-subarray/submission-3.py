class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        currmin,currmax = 1,1

        for n in nums:
            temp = currmax*n
            currmax = max(temp,currmin*n,n)
            currmin = min(temp,currmin*n,n)
            res = max(currmax,res)

        return res