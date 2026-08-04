class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
                return nums[0]
        n = len(nums)
        def helper(inums):
            if len(inums) == 1:
                return inums[0]
            dp = [0] *len(inums)
            dp[0],dp[1] = inums[0], max(inums[0],inums[1])

            for i in range(2,len(inums)):
                dp[i] = max(dp[i-1], inums[i]+dp[i-2])

            return dp[-1]
        return max(helper(nums[:-1]), helper(nums[1:]))

      