class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def subarray(n):
            cs=0
            count=1
            for i in range(len(nums)):
                if cs+nums[i]<=n:
                    cs+=nums[i]
                else:
                    count+=1
                    cs=nums[i]
            return count
        l=max(nums)
        h=sum(nums)
        ans=max(nums)
        while l<=h:
            m=(l+h)//2
            if subarray(m)<=k:
                ans=m
                h=m-1
            else:
                l=m+1
        return ans
                


