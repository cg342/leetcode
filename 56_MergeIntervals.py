class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        res = []

        start, end = sorted_intervals[0]
    
        for s, e in sorted_intervals:
            if s <= end:
                end = max(end, e)
            else: 
                res.append([start,end])
                start, end = s, e
        res.append([start, end])                   
        
        return res