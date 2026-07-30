class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda z:z[0])
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                start = min(res[-1][0],intervals[i][0])
                end = max(res[-1][1],intervals[i][1])
                res[-1] = [start,end]
            else:
                res.append(intervals[i])

        return list(res)