class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r=0
        if target >max(nums):
            return len(nums)
        else:
            for i in range(len(nums)):
            
                if target<=nums[i]:
                    r=i
                    break
        return r