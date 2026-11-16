class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r= 1,max(piles)
        res = r
        while l <= r:
            eatfreq = (l+r)//2
            eatcount = 0
            for p in piles:
                eatcount += math.ceil(p/eatfreq)
            
            if eatcount <= h:
                res = eatfreq
                r = eatfreq - 1
            else:
                l = eatfreq + 1

        return res

