class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count=0
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]==val and nums[r]!=val:
                nums[l],nums[r]=nums[r],nums[l]
                count+=1
                r-=1
            if nums[l] != val:
                l+=1
            if nums[r] == val:
                r-=1
        return l
    



