class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = len(intervals)
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if start <= s <= end and start <= e <= end or s <= start <= e and s <= end <= e:
                res -= 1
                start = min(start, s)
                end = max(end, e)
            else:
                start = s
                end = e
        return res
                