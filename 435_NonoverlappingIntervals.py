class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if not intervals:
            return res
        
        intervals.sort(key = lambda x:x[1])
        end = intervals[0][1]
        

        for s, e in intervals[1:]:
            if s >= end:
                end = e
            else:
                res += 1
        return res
                