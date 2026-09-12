class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long, maxlen = 0, 0
        seen = set(nums)

        for num in nums:
            if num-1 not in seen:
                long = 1
                while num+long in seen:
                    long+=1
                maxlen = max(maxlen,long)

        return maxlen

                