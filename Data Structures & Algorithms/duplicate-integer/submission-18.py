class Solution:
    def hasDuplicate(self, nums:[int]) -> bool:
        have = set()
        for num in nums:
            if num in have:
                return True
            else:
                have.add(num)
        return False