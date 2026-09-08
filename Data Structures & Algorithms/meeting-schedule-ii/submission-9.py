"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key=lambda x:x.start)
        mroom = room = 0
        start = end = 0
        allstart = sorted(interval.start for interval in intervals)
        allends = sorted(interval.end for interval in intervals)

        for _ in range(len(intervals)):
            if allstart[start] < allends[end]:
                start+=1
                room +=1

            else:
                end+=1
                room-=1
            
            mroom = max(mroom, room)

        return mroom