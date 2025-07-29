class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in nums:
            j=abs(i)-1
            if nums[j]>0:
                nums[j]= -nums[j]      
        m=[]
        for i in range(len(nums)):
            if nums[i]>0:
                m.append(i+1)
        return m