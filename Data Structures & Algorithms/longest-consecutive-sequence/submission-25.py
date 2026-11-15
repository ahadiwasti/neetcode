class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest = long = 0

        for num in nums:
            if num-1 not in seen:
                long = 1
                while num+long in seen:
                    long+=1
                longest = max(longest,long)

        return longest