class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[index] = nums[r]
                index+=1
        return index
