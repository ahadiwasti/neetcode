class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for idx,num in enumerate(nums):
            if num not in seen:
                seen[num] = idx

            else:
                if abs(seen[num]-idx) <= k:
                    return True
                else:
                    seen[num] = idx

        return False