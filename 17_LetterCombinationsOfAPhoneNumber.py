class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        if digits == '':
            return []
        elif len(digits) == 1:
            for l in letter[int(digits)-2]:
                res.append(l)
            return res
        
        rest = digits[1:]
        for j in letter[int(digits[0])-2]:
            for r in self.letterCombinations(rest):
                res.append(j + r)
        return res