class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currprofit,buyat = 0,prices[0]

        for p in range(1,len(prices)):
            if buyat > prices[p]:
                buyat = prices[p]

            currprofit = max(currprofit, prices[p]-buyat)

        return currprofit