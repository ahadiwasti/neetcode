class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum = 0
        reslen = float('inf')
        l = 0

        for r in range(len(nums)):
            currsum += nums[r]

            while currsum >= target:
                if r-l+1 < reslen:
                    reslen = r-l+1
                currsum -= nums[l]
                l+=1

        return reslen if reslen != float('inf') else 0

