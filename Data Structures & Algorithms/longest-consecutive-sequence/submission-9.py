class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)
        for n in nums:
            if n - 1 not in seen:
                longest = 1
                while n+longest in seen:
                    longest +=1
                res = max(res,longest)
        return res