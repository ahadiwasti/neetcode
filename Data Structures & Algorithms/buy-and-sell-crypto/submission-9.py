class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyat = prices[0]
        maxprofit = 0

        for p in prices:
            if p < buyat:
                buyat = p


            maxprofit = max(maxprofit , p-buyat)


        return maxprofit