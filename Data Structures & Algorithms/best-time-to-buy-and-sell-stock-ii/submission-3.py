class Solution:
    def maxProfit(self, prices:List[int])->int:
        profit = 0
        buyat = prices[0]

        for price in prices:
            if price > buyat:
                profit += price-buyat
            buyat = price

        return profit