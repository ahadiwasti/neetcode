"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        room, maxroom, start,end =0,0,0,0

        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        for _ in range(len(intervals)):
            if starts[start] < ends[end]:
                start+=1
                room+=1
            else:
                end+=1
                room-=1

            maxroom = max(maxroom, room)

        return maxroom