class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r= max(weights), sum(weights)
        res = r

        while l <= r:
            capacity = (l+r)//2
            daycount = 1
            currload = 0
            for wei in weights:
                if currload + wei > capacity:
                    daycount +=1
                    currload = 0
                currload += wei
                
            if daycount <= days:
                r = capacity -1
                res = capacity
            else:
                l = capacity +1

        return res