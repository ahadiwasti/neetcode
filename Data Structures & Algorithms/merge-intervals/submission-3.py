class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)
        mp = [0]*(max_val+1)

        start,end = -1,-1

        for s,e in intervals:
            mp[s] = max(e+1,mp[s])
        
        res = []

        for i in range(len(mp)):
            if mp[i] != 0:
                if start == -1:
                    start = i
                end = max(mp[i]-1,end)

            if end == i:
                res.append([start,end])
                start,end = -1,-1

        if start != -1:
            res.append([start,end])
        
        return res

