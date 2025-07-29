class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        diff=0
       
        for i,v in enumerate(nums):
            diff=target-v
            if diff in d:
                return [i,d[diff]]
               
                
            d[v]=i
        
        
                
            