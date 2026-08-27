class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        maxl = 0

        for num in nums:
            if num-1 not in seen:
                longest = 1
                while num+longest in seen:
                    longest+=1
                maxl = max(longest, maxl)

        return maxl