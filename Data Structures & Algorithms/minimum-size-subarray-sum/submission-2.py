class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=r=0

        currsum,reslen = 0,float('inf')

        while r < len(nums):
            currsum+=nums[r]

            while currsum >= target:
                reslen = min(r-l+1,reslen)
                currsum-=nums[l]
                l+=1
            r+=1

        return reslen if reslen != float('inf') else 0