class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = res = 0
        seen = {0:1}
        for r in range(len(nums)):
            curr += nums[r]
            diff =  curr - k
            res += seen.get(diff,0)
            seen[curr] = 1 + seen.get(curr,0)
        return res