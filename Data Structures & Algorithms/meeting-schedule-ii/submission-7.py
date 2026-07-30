"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=end=maxroom=room = 0

        startTimes = sorted(interval.start for interval in intervals)
        endTimes = sorted(interval.end for interval in intervals)


        for _ in range(len(intervals)):
            if startTimes[start] < endTimes[end]:
                start+=1
                room+=1

            else:
                end+=1
                room-=1

            maxroom= max(maxroom,room)

        return maxroom