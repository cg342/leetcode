class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(sub, ind):
            if len(sub) == k:
                res.append(sub)
                return
            for i in range(ind, n + 1):
                dfs(sub + [i], i + 1)

                
        res = []
        dfs([], 1)
        return res