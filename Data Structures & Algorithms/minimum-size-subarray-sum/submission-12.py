class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum = 0
        l = 0
        minlen = float('inf')
        for r in range(len(nums)):
            currsum += nums[r]
            while currsum >= target:
                minlen = min(r-l+1, minlen)
                currsum-=nums[l]
                l+=1 
        return minlen if minlen != float('inf') else 0
