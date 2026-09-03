class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum = 0 
        currlen = float('inf')
        l=r=0
        while r < len(nums):
            currsum += nums[r]
            while currsum >= target:
                currsum -= nums[l]
                currlen = min(currlen, r-l+1)
                l+=1
            r+=1
        
        return currlen if currlen != float('inf') else 0


T:O(n)
S:O(1)