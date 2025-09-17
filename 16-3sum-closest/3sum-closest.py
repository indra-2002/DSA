class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        r=len(nums)-1
        cs=0
        l=0
        mi=float("inf")
        for i in range(len(nums)-2):
            r=len(nums)-1
        
            l=i+1
            while l<r:
                
                cs=nums[i]+nums[l]+nums[r]
                if abs(cs - target) < abs(mi - target):
                    mi=cs
                if cs>target:
                    r-=1

                elif cs< target:
                    l+=1

                else:

                    return cs
        return mi


