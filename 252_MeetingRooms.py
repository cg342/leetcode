class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key = lambda x:x[0])
        curr = intervals[0][1]
        
        for interval in intervals[1:]:
            if curr > interval[0]:
                return False
            curr = interval[1]
        
        return True
        
        
        