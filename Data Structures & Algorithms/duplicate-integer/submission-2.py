class Solution:
    def hasDuplicate(self,nums: list[int]) -> bool:
        seen = set()
        for val in nums:
            if val in seen:
                return True
            seen.add(val)
        return False
