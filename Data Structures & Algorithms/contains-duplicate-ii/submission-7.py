class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for id,num in enumerate(nums):
            if num in seen:
                if abs(seen[num]-id) <= k:
                    return True
                else:
                    seen[num] = id
            else:
                seen[num] = id

        return False