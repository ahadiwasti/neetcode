class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyat = prices[0]
        currmax = 0

        for p in prices:
            if p < buyat:
                buyat = p
            currmax = max(currmax, p-buyat)

        return currmax
            