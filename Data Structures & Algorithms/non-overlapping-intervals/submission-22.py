class Solution:
    def eraseOverlapIntervals(self,intervals:List[Interval])-> int:
        count = 0
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[0])
        currEnd = intervals[0][1]

        for i in range(1,len(intervals)):
            if currEnd > intervals[i][0]:
                count +=1
                currEnd = min(currEnd, intervals[i][1])
            else:
                currEnd = intervals[i][1]

        return count