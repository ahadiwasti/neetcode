class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r= 0
        minSumLen,currSum = float('inf'),0
        while r < len(nums):
            currSum+=nums[r]
            while currSum >= target:
                minSumLen= min(r-l+1,minSumLen)
                currSum-=nums[l]
                l+=1
            r+=1

        return minSumLen if minSumLen != float('inf') else 0

