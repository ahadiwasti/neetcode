class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[index] = nums[r]
                index+=1

        return index