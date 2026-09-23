class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx,num in enumerate(nums):
            if target-num in mp:
                return [mp[target-num], idx]
            
            else:
                mp[num] = idx
        return []