class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def count(g):
            if g<0:
                return 0
            l=0
            s=0
            res=0
            for r in range(len(nums)):
                s+=nums[r]
                while s>g:
                    s-=nums[l]
                    l+=1
                res+=r-l+1
            return res
        return count(goal)-count(goal-1)