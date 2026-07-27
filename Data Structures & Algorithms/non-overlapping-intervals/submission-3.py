class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        res = 0
        currMax = intervals[0][1]
        for start,end in intervals[1:]:
            if currMax > start:
                currMax = min(end,currMax)
                res+=1
            else:
                currMax = end
            
        return res