class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyat = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] < buyat:
                buyat = prices[i]
            profit = max(profit, prices[i]-buyat)
        return profit        
