class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        currsum,currlen=0,float('inf')
        while r < len(nums):
            currsum+=nums[r]
            while currsum >= target:
                currsum-=nums[l]
                currlen = min(currlen,r-l+1)
                l+=1   

            r+=1

        return currlen if currlen != float('inf') else 0 


