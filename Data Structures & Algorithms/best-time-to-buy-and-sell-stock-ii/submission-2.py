class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyat = prices[0]
        profit = 0
        for p in prices:
            if p > buyat:
                profit += p-buyat

            buyat = p

        return profit