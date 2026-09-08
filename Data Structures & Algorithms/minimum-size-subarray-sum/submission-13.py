class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        l=0
        reslen = float('inf')
        for r in range(len(nums)):
            curr+=nums[r]
            while curr>=target:
                reslen = min(reslen,r-l+1)
                curr-=nums[l]
                l+=1
           

        return reslen if reslen != float('inf') else 0
