class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        res = []
        start, end = 0, 0
        d = {S[i]:i for i in range(len(S))}
        
        for i in range(len(S)):
            end = max(end, d[S[i]])
            if i == end:
                res.append(end-start+1)
                start = i + 1
        return res