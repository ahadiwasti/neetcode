class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        currsum,minlen = 0,float('inf')
        while  r < len(nums):
            currsum +=nums[r]

            while currsum >= target:
                minlen = min(r-l+1,minlen)
                currsum -=nums[l]
                l+=1
            r+=1

        return minlen if minlen != float('inf') else 0