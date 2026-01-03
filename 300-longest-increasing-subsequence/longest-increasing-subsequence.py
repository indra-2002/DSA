class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[]
        def lower(element,res):
            l=0
            r=len(res)-1
            ans=len(res)
            while l<=r:
                m=(l+r)//2
                if res[m]>=element:
                    ans=m
                    r=m-1
                else:
                    l=m+1
            return ans
        for i in range(len(nums)):
            index=lower(nums[i],res)
            if index==len(res):
                res.append(nums[i])
            else:
                res[index]=nums[i]
        return len(res)
