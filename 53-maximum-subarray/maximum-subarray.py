class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=0
        ms=nums[0]
        cs=0
        for r in range(len(nums)):
            cs+=nums[r]
            
            ms=max(ms,cs)
            if cs<0:
                cs=0
        return ms
