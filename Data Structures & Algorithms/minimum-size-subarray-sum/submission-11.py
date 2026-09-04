class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum = 0
        minlen = float('inf')
        l = 0

        for r in range(len(nums)):
            currsum += nums[r]

            while currsum >= target:
                minlen = min(minlen,r-l+1)
                currsum-=nums[l]
                l+=1
        return minlen if minlen != float('inf') else 0
