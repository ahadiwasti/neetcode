class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        reslen = float('inf')
        currsum = 0
        l,r = 0,0

        while r < len(nums):
            currsum += nums[r]
            while currsum >= target:
                reslen = min(reslen, r-l+1)
                currsum -= nums[l]
                l+=1
            r+=1
        return reslen if reslen != float('inf') else 0

T:O(n)
S:O(1)