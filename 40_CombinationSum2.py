class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def dfs(sub, currSum, ind):
            if currSum == target and sorted(sub) not in res:
                res.append(sorted(sub))
                return
            if currSum > target:
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                dfs(sub + [candidates[i]], currSum+candidates[i], i+1)
                
        res = []
        dfs([], 0, 0)
        return res
    
    