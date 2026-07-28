class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax,buyAt = 0,prices[0]

        for p in range(1,len(prices)):

            if buyAt > prices[p]:
                buyAt = prices[p]
            
            currentMax = max(currentMax, prices[p]-buyAt)

        return currentMax