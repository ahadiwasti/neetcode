class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = l = 0

        res = float('inf')

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                if (r-l+1) < res:
                    res = r-l+1
                curr -= nums[l]
                l+=1
        return res if res != float('inf') else 0