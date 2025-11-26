class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        mini=float('inf')
        if l==h:
            return nums[l]
        while l<=h:
            mid=(l+h)//2
            
            if nums[mid] >nums[h]:
                
                l=mid+1

            elif nums[mid] < nums[h]:
                
                h=mid
            else:
                h-=1
        return nums[l]
