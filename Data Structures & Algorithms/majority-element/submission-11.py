class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = float('inf')

        for i in range(len(nums)):
            if count == 0:
                val = nums[i]
            count += (1 if val == nums[i] else -1)

        return val


                