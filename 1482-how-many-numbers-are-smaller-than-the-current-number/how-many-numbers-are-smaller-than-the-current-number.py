class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t=nums[:]
        nums.sort()
        d={}
        r=[]
        for i,v in enumerate(nums):
            if v not in d:
                d[v]=i
        for i in t:
            r.append(d[i])
        return r