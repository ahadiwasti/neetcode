class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0

        seen = {0:1}

        for num in nums:
            currsum += num
            diff = currsum - k

            res += seen.get(diff,0)

            seen[currsum] = 1+seen.get(currsum,0)

        return res