class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        free = []
        intervals.sort(key = lambda x:x[0])
        heapq.heappush(free, intervals[0][1])
        
        for inter in intervals[1:]:
            if free[0] <= inter[0]:
                heapq.heappop(free)
            
            heapq.heappush(free, inter[1])
        
        return len(free)