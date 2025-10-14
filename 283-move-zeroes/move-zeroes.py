class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[insert]=nums[i]
                insert+=1
            if i==len(nums)-1:
                while insert<len(nums):
                    nums[insert]=0
                    insert+=1
                
                
        return nums

