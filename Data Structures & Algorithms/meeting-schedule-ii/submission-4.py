"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s,e,room,maxroom = 0,0,0,0
        startTimes = sorted(interval.start for interval in intervals)
        endTimes = sorted(interval.end for interval in intervals)

        for _ in intervals:
            if startTimes[s] < endTimes[e]:
                s+=1
                room+=1
            else:
                room-=1
                e+=1
            
            maxroom = max(room,maxroom)
        
        return maxroom

