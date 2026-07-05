class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)
        mp = [0]*(max_val+1)

        for start,end in intervals:
            mp[start] = max(end+1,mp[start])
        start_val = -1
        end_val = -1
        res = []

        for i in range(len(mp)):
            if mp[i] != 0:
                if start_val == -1:
                    start_val = i
                end_val = max(mp[i]-1,end_val)
            
            if end_val == i:
                res.append([start_val,end_val])
                start_val = -1
                end_val = -1

        if start_val != -1:
            res.append([start_val,end_val])
        return res
