class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin,currMax = 1,1
        for n in nums:
            temp = n*currMax
            currMax = max(temp,currMin*n,n)
            currMin = min(temp,currMin*n,n)
            res = max(currMax,res)
        return res