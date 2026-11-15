class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        num = nums[0]
        for i in range(len(nums)):
            if count == 0:
                num = nums[i]
            count +=(1 if num == nums[i] else -1)

        return num