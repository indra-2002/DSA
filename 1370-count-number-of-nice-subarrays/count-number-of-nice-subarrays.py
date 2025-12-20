class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        def count(g):
            if g<0:
                return 0
            s=0
            l=0
            res=0
            for i in range(len(nums)):
                s+=nums[i]
                while s>g:
                    s-=nums[l]
                    l+=1
                res+=i-l+1
            return res
        return count(k)-count(k-1)