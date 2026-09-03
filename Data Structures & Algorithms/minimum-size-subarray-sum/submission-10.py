class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=currsum= 0
        reslen = float('inf')

        for r in range(len(nums)):
            currsum+=nums[r]
            while currsum >= target:
                reslen = min(reslen, r-l+1)
                currsum-=nums[l]
                l+=1
        
        return reslen if reslen != float('inf') else 0

# T:O(n)
# S:O(1)
