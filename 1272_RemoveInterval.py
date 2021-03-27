class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        # i, j = 0, 0
        start, end = toBeRemoved
        for s, e in intervals:
            # intervals [2,3]   toBeRemoved [1,9]
            # intervals [1,3]   toBeRemoved [2,5]
            if s < start < e:
                res.append([s, min(start, e)])
            if s < end < e:
                res.append([max(s, end),e])
            if start >= e or end <= s:
                res.append([s, e])            
        return res