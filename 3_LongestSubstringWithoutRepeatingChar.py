class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxlength = 0
        dt = {}
        
        for i in range(len(s)):
            if s[i] in dt:
                start = max(start, dt[s[i]]+1)
            maxlength = max(maxlength, i-start+1)
            dt[s[i]] = i
        
        return maxlength