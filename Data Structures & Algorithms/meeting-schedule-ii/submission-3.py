"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key = lambda x:x.start)
        heap = []
        for i in range(len(intervals)):
            if not heap: #only happens when i == 0
                heapq.heappush(heap, intervals[i].end)
                continue
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap) #pop the unusued room
            heapq.heappush(heap, intervals[i].end) #add the used room
        return len(heap)