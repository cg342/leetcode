class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        dt = collections.defaultdict(int)
        count = 0
        
        for t in time:
            if t % 60 == 0:
                count += dt[0]
            else:
                count += dt[60-t%60]
            dt[t%60] += 1
            
        return count
        