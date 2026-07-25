class Solution:
    def hasDuplicate(self, nums:[int]) -> bool:
        seen = {}
        for n in nums:
            if n in seen:
                return seen[n]
            seen[n] = True
        return False