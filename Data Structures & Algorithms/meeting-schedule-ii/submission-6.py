"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes=sorted(interval.start for interval in intervals)
        endTimes=sorted(interval.end for interval in intervals)
        start=end=room=maxroom = 0
        for _ in intervals:
            if startTimes[start] < endTimes[end]:
                start+=1
                room+=1
            else:
                room-=1
                end+=1

            maxroom = max(maxroom,room)

        return maxroom
