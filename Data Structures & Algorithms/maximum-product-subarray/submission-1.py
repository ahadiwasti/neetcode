class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin,currMax = 1,1
        for n in nums:
            maxval = n * currMax
            currMax = max(maxval,n*currMin,n)
            currMin = min(maxval,n*currMin,n)
            res = max(res, currMax)
        return res