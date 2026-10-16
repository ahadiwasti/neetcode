class Solution:
    def eraseOverlapIntervals(self,intervals:List[Interval])-> int:
        intervals.sort(key=lambda x:x[0])
        currmax = intervals[0][1]
        overlap = 0

        for i in range(1, len(intervals)):
            if currmax > intervals[i][0]:
                overlap +=1
                currmax = min(currmax, intervals[i][1])
            else:
                currmax = intervals[i][1]
        return overlap
