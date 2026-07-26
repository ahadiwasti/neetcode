class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat=0
        l,r = 0,len(people)-1
        maxweight = max(people)
        freq = [0] * (maxweight+1)
        for p in people:
            freq[p]+=1
        
        idx, weight = 0,1
        while idx < len(people):
            while freq[weight] == 0:
                weight+=1
            people[idx] = weight
            freq[weight]-=1
            idx+=1

        while l <= r:
            diff = limit - people[r]
            boat +=1
            r-=1

            if diff >= people[l]:
                l+=1
        return boat

