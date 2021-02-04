class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        res = []
        nums[:] = sorted(nums)
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            for r in self.permuteUnique(rest):
                if [nums[i]] + r not in res:
                    res.append([nums[i]] + r)
    
        return res