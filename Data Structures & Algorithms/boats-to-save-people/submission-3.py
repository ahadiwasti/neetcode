class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat=0
        l,r = 0,len(people)-1

        while l <= r:
            diff = limit - people[r]
            boat +=1
            r-=1

            if diff >= people[l]:
                l+=1
        return boat

