class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        res = [0] * numLen*2
        for i in range(len(nums)):
            res[i] = res[i+numLen] = nums[i]
        return res