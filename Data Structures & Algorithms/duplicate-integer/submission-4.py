class Solution:
    def hasDuplicate(self, nums:[int]) -> bool:
        seen = set()
        for item in nums:
            if item in seen:
                return True
            seen.add(item)
        return False

