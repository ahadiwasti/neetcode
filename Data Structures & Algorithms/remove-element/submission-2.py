class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[i] = nums[idx]
                i+=1
        return i
        
