class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        l,r= 0 , len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l+=1
                r-=1
                continue

            if nums[l] <= nums[mid]:
                if nums[l] > target or nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1 

            else:
                if nums[r] < target or nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1

        return False


            
            
