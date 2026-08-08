class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        return max(self.maxRob(nums[1:]), self.maxRob(nums[:-1]))
    def maxRob(self,num):
        if len(num) <= 1:
            return num[0]

        n = len(num)
        dp = [0] * n
        dp[0], dp[1] = num[0], max(num[0], num[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1], num[i]+dp[i-2])

        return dp[-1]