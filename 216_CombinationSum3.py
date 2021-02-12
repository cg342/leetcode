class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def dfs(sub, ind, sum):
            if len(sub) == k and sum == n and sorted(sub) not in res:
                res.append(sorted(sub))
            for i in range(ind, 10):
                if i not in sub:
                    dfs(sub + [i], ind+1, sum + i)
        res = []        
        dfs([], 1, 0)
        return res
    