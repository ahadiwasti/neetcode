class Solution:
    def eraseOverlapIntervals(self,intervals:List[Interval])-> int:
        intervals.sort(key=lambda x:x[0])
        count = 0
        currMax = intervals[0][1]
        for i in range(1,len(intervals)):
            if currMax > intervals[i][0]:
                count +=1
                currMax = min(currMax,intervals[i][1])
            else:
                currMax = intervals[i][1]

        return count