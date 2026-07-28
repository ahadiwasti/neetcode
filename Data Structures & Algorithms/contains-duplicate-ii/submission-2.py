class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for j,num in enumerate(nums):
            if num not in seen:
                seen[num] = j
            elif abs(seen[num]-j) <= k:
                    return True
            else:
                seen[num] = j
        
        return False

