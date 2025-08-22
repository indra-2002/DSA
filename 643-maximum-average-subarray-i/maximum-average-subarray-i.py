class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        m=float('-inf')
        cs=0
        l=0
        for i in range(len(nums)):
            cs+=nums[i]
            if i-l+1==k:
                m=max(m,cs*1.0/k)
                cs-=nums[l]
                l+=1
        return m

