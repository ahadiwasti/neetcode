class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)

        res = r

        while l <= r:
            capacity = (l+r)//2

            dayCount = 1
            currLoad = 0

            for wei in weights:
                if currLoad+wei > capacity:
                    dayCount +=1
                    currLoad = 0

                currLoad+=wei

            if dayCount <= days:
                res = capacity
                r = capacity -1

            else:
                l = capacity +1

        return res 
