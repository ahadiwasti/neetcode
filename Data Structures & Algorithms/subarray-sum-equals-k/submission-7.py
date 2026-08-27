class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curr = 0
        seen = {0:1}
        for num in nums:
            curr += num
            diff = curr-k
            res += seen.get(diff,0)
            seen[curr] = 1 + seen.get(curr,0)

        return res