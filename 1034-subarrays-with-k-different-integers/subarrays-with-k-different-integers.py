class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count(goal):
            l=s=res=0
            c={}
            if goal<0:
                return 0
            for i in range(len(nums)):
                if nums[i] not in c:
                    c[nums[i]]=1
                else:
                    c[nums[i]]+=1
                while len(c)>goal:
                    c[nums[l]]-=1
                    if c[nums[l]]==0:
                        del c[nums[l]]
                    l+=1
                res+=i-l+1
            return res
        return count(k)-count(k-1)
