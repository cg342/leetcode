class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(sub):
            if sum(sub) == target and sorted(sub) not in res:
                    res.append(sorted(sub))
                    return
            if sum(sub) > target:
                return
            for i in range(len(candidates)):
                dfs(sub + [candidates[i]])
            
        res = []
        dfs([])
        return res
        