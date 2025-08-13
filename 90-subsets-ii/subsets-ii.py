class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        res=[]
        sol=[]
        def backtrack(start):
            res.append(sol[:])

            for i in range(start,n):
                if i>start and nums[i]==nums[i-1]:
                    continue
                sol.append(nums[i])
                backtrack(i+1)
                sol.pop()
        backtrack(0)
        return res
                

            