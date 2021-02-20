class Solution:
    def partition(self, s: str) -> List[List[str]]:

        
        def isPalindrome(string):
            return string == string[::-1]

        
        def helper(sub, word):
            if not word:
                res.append(sub)
                return
            for i in range(1, len(word)+1):
                if isPalindrome(word[:i]):
                    helper(sub+[word[:i]], word[i:])

        res = []
        helper([],s)
        return res