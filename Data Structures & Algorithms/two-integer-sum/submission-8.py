class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        
        for idx,val in enumerate(nums):
            if target - val in seen:
                return [seen[target-val], idx]
            seen[val] = idx
        