class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}

        res = curr = 0

        for num in nums:
            curr += num
            diff = curr - k

            res += seen.get(diff,0)

            seen[curr] = 1 + seen.get(curr,0)

        return res
