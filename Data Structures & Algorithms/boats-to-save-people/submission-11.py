class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        l,r = 0,len(people)-1
        
        freq = defaultdict(int)
        for p in people:
            freq[p]+=1

        minval,maxval = min(people), max(people)

        index = 0
        for i in range(minval,maxval+1):
            while freq[i]:
                people[index] = i
                freq[i]-=1
                index +=1

        while l<=r:
            diff = limit - people[r]
            boat +=1
            r-=1

            if diff >= people[l]:
                l+=1

        return boat

# T:O(n)
# S:O(m)
