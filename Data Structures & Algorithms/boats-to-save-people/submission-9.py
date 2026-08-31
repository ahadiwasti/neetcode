class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        minval,maxval = min(people), max(people)
        freq = defaultdict(int)
        for p in people:
            freq[p]+=1
        index = 0
        for i in range(minval,maxval+1):
            while freq[i]:
                people[index] = i
                index +=1
                freq[i] -=1

        boat = 0
        l,r = 0,len(people)-1
        while l <= r:
            diff = limit-people[r]
            boat+=1
            r-=1

            if diff >= people[l]:
                l+=1

        return boat