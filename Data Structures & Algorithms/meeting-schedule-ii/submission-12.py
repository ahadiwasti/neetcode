"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)
        maxroom=start=end=room = 0

        for _ in range(len(intervals)):
            if starts[start] < ends[end]:
                room+=1
                start+=1
            else:
                room-=1
                end+=1
            maxroom = max(maxroom,room)

        return maxroom

