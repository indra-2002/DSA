class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        l=0
        nums.sort()
        for i in range(len(nums)):
            while nums[i]-nums[l]>1:
                l+=1
            if nums[i]-nums[l]==1:
                res=max(res,i-l+1)

        return res
