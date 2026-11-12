class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = r
        while l <= r:
            mid = (l+r)//2
            eatCount = 0

            for p in piles:
                eatCount += math.ceil(p/mid)

            if eatCount <= h:
                res = mid
                r = mid - 1

            else:
                l = mid + 1
        return res

    # O(n * log(m))
