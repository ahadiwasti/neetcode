class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = curr = 0

        for num in nums:
            if count == 0:
                curr = num
            count += (1 if curr == num else -1)

        return curr 