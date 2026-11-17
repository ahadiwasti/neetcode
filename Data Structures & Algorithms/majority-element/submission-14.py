class Solution:
    def majorityElement(self, nums)-> int:
        val = count = 0
        for num in nums:
            if count == 0:
                val = num
            count += (1 if val == num else -1)
        return val
