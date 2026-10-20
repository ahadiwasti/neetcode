class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyat = prices[0]
        profit = 0
        for price in prices[1:]:
            if price > buyat:
                profit += price - buyat
            buyat = price
        return profit