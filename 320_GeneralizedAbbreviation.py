class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def helper(sub, rest):
            if len(rest) == 0:
                res.append(sub)
                return
            
            if sub and sub[-1].isdigit():
                helper(sub[:-1]+str(int(sub[-1])+1), rest[1:])
            else:
                helper(sub+'1',rest[1:])
            helper(sub+rest[0], rest[1:])
            
            
        res = []
        helper('',word)
        return res
    
    