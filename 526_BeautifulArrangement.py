class Solution:
    def countArrangement(self, n: int) -> int:
        
        nums = [i for i in range(1, n+1)]    
        def helper(sub, ind, nums):
            
            if len(sub) == n:
                res.append(sub)
                return
                 
            for i in range(len(nums)):
                if nums[i] % ind == 0 or ind % nums[i] == 0:
                    helper(sub+[nums[i]], ind+1, nums[:i] + nums[i+1:])
            
        res = []
        helper([], 1, nums)
        return len(res)
            
            
        