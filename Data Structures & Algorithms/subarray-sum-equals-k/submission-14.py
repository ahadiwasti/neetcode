class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        currtotal = total = 0

        for num in nums:
            currtotal += num
            diff = currtotal - k

            total += seen.get(diff,0)
            seen[currtotal] =1+seen.get(currtotal,0)

        return total
