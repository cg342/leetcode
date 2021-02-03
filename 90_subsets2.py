class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for n in sorted(nums):
            for i in range(len(res)):
                if [n] + res[i] not in res:
                    res.append([n] + res[i])
        return res
                