class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):

            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left,right = i+1, len(nums)-1

            while left < right:
                threesum = nums[left]+nums[right]+nums[i]
                if threesum == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif threesum > 0:
                    right -=1
                else:
                    left+=1
        return res
