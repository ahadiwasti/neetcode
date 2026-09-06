class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for idx,num in enumerate(nums):
            if num in seen:
                if abs(seen[num]-idx) <= k :
                    return True
                else:
                    seen[num] = idx
            else:
                seen[num] = idx

        return False