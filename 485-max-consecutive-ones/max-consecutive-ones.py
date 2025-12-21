class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=float('-inf')
        l=0
        for i in range(len(nums)):
            if nums[i]==0:
                l=i+1
            maxi=max(maxi,i-l+  1)
        return maxi
            
