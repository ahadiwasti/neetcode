class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmax = 0
        buyat = float('inf')

        for i in range(len(prices)):
            if prices[i] < buyat:
                buyat = prices[i]
            currmax = max(prices[i]-buyat,currmax)
        return currmax