class Solution:
    def maxProfit(self, prices:List[int])->int:
        buyat = prices[0]
        profit = 0
        for p in range(1, len(prices)):
            if prices[p] > buyat:
                profit += prices[p]-buyat
            buyat = prices[p]
        return profit
