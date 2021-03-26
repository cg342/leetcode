class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            si, ei = firstList[i]
            sj, ej = secondList[j]
            
            if si <= sj <= ei or sj <= si <= ej:
                start = max(si, sj)
                end = min(ei, ej)
                res.append([start, end])
            if ei < ej:
                i += 1
            elif ej <=ei:
                j += 1
        return res
                