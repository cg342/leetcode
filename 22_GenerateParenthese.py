class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(sub,left, right):
            if left == right == 0:
                res.append(sub)
                return
            if left < 0 or right < 0 or left > right:
                return
            helper(sub+'(', left-1, right)
            helper(sub+')', left, right-1)
                                
        
        res = []
        helper('',n,n)
        return res