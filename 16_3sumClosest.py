class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')    
        
        # [-1,2,1,-4]
        nums.sort()
        
        for i in range(len(nums)-2):
            lo = i + 1
            hi = len(nums)-1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if abs(summ - target) < abs(closest):
                    closest = target - summ
                if summ < target:
                    lo += 1
                else:
                    hi -= 1
            if closest == 0:
                break
        return target - closest