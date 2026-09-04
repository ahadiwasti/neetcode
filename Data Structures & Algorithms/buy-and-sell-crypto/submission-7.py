class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyat = float('inf')
        currmax = 0

        for p in prices:
            if p < buyat:
                buyat = p
            currmax = max(currmax, p-buyat)

        return currmax
            
    T:O(n)
    S:O(1)