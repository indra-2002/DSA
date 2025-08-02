class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        m=float('inf')
        s=0
        total=0
        l=0
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                m=min(m,i-l+1)
                total-=nums[l]
                l+=1
        if m==float('inf'): return 0

        else: return m
