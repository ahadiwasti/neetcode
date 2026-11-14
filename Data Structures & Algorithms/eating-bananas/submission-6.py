class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r, = 1 ,  max(piles)
        res = r
        while l <=r:
            eatrate = (l+r)//2
            eatcount = 0
            for p in piles:
                eatcount += math.ceil(p/eatrate)

            if eatcount <= h:
                res = eatrate
                r = eatrate -1

            else:
                l = eatrate +1

        return res 