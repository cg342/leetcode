class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        def helper(sub, ind):
            if len(sub) == len(S):
                res.append(sub)
                return
            if S[ind].isalpha():
                helper(sub+S[ind].upper(), ind+1)
                helper(sub+S[ind].lower(), ind+1)
            else:
                helper(sub+S[ind], ind+1)    
            
        res = []
        helper('', 0)
        return res
                