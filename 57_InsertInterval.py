class Solution:
    def insert(self, intervals, new):
        if not intervals:
            return [new]
        
        intervals.sort(key = lambda x:x[0])
        start, end = new
        res = []
        for s, e in intervals:
            if s <= start <= e or start <= s <= end:
                start = min(s, start)
                end = max(e, end)
            else:
                res.append([s, e])
                
        res.append([start, end])
        return sorted(res, key = lambda x:x[0])