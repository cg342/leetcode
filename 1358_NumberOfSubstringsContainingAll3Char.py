class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        maxA, maxB, maxC, ans = 0,0,0,0
        
        for i in range(len(s)):
            if s[i] == 'a':
                maxA = i + 1
            elif s[i] == 'b':
                maxB = i + 1
            elif s[i] == 'c':
                maxC = i + 1
            
            
            ans += min(maxA, maxB, maxC)
        
        return ans