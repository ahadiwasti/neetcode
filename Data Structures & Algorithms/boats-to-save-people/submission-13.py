class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        l,r = 0,len(people)-1
        people.sort()

        if not people:
            return 0

        while l <=r:
            diff = limit-people[r]
            boat+=1
            r-=1

            if diff >= people[l]:
                l+=1
        return boat


# T:O(n)
# S:O(m)
