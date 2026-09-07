class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyat = prices[0]
        maxp = 0
        for p in prices:
            if p < buyat:
                buyat = p
            maxp = max(maxp, p-buyat)

        return maxp

            