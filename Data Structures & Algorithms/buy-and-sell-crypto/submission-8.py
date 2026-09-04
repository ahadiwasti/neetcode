class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyat = prices[0]
        curr = 0

        for p in prices:
            if p < buyat:
                buyat = p

            curr = max(curr, p - buyat)

        return curr