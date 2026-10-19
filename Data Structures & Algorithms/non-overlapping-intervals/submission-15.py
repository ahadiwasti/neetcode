class Solution:
    def eraseOverlapIntervals(self,intervals:List[Interval])-> int:
        intervals.sort(key=lambda x:x[0])
        count = 0
        currend = intervals[0][1]

        for i in range(1,len(intervals)):
            if currend > intervals[i][0]:
                count +=1
                currend = min(intervals[i][1],currend)

            else:
                currend = intervals[i][1]

        return count