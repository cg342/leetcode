class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            for r in self.permute(rest):
                res.append([nums[i]] + r)
        
        return res