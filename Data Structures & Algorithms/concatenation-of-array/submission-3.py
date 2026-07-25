class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nLen = len(nums)
        res = [0] * (nLen*2)
        print(res)
        for i in range(len(nums)):
            res[i] = res[i+nLen] = nums[i]

        return res 
        