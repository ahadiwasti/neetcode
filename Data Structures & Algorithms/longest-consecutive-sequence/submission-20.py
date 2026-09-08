class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        maxres = 0
        seen = set(nums)

        for num in nums:
            if num-1 not in seen:
                longest = 1
                while num+longest in seen:
                    longest+=1
                
                maxres = max(maxres, longest)

        return maxres
            