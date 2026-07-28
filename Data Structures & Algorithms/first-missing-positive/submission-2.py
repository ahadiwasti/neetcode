class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i,n=0,len(nums)

        while i<n:
            if nums[i] <= 0 or nums[i] > n:
                i+=1
                continue
            index = nums[i]-1
            if nums[i] != nums[index]:
                nums[i],nums[index] = nums[index],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]-1 != i:
                return i+1
        
        return n+1