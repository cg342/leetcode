class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dt = {}
        
        for string in strs:
            st = ''.join(sorted(string)) 
            dt[st] = dt.get(st, []) + [string]
        
        return dt.values()
            