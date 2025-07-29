class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u=0
        for i in nums:
            u^=i
        return u
        