class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        
        for n in nums:
            for i in range(len(res)):
                res.append([n] + res[i])
        
        return res