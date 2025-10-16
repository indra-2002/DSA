class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        value=nums[0]
        count=0
        for i in range(len(nums)):
            if count==0:
                value=nums[i]
            if nums[i]==value:
                count+=1
            else:
                count-=1
                
            
        return value
                