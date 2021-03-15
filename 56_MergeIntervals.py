class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals[:] = sorted(intervals, key=lambda x:x[0])
        res = []
        if len(intervals) == 1:
            return intervals
        bound = intervals[0]
    
        for i in range(len(intervals)):
            if intervals[i][0] <= bound[1]:
                bound = [bound[0], max(bound[1], intervals[i][1])]
            else: 
                res.append(bound)
                bound = intervals[i]
        res.append(bound)                   
        
        return res
            