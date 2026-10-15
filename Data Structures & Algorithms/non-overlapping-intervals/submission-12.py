class Solution:
    def eraseOverlapIntervals(self,intervals:List[Interval])-> int:
        intervals.sort(key=lambda x:x[0])
        currend = intervals[0][1]
        overlap = 0
        for start,end in intervals[1:]:
            if currend > start:
                 overlap+=1
                 currend = min(currend, end)

            else:
                currend= end
        return overlap