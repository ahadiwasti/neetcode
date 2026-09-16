"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        mstart = sorted(interval.start for interval in intervals)
        mend = sorted(interval.end for interval in intervals)

        maxroom = room = end = start = 0

        for _ in range(len(intervals)):
            if mstart[start] < mend[end]:
                start+=1
                room+=1

            else:
                end+=1
                room-=1

            maxroom = max(maxroom,room)

        return maxroom

