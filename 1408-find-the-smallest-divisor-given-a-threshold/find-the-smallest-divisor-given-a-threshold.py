class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        h=ans=max(nums)
        while l<=h:
            mid=(l+h)//2
            total=0
            for i in nums:
                total+=math.ceil(i/mid)
            if total<=threshold:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans