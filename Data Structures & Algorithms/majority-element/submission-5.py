class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        currchar = 0

        for num in nums:
            if count == 0:
                currchar = num

            count += (1 if currchar == num else -1)

        return currchar