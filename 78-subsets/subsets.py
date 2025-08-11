class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        r=[]
        s=[]
        def backtrack(i):
            if i==n:
                r.append(s[:])
                return 
            # without nums[i]
            backtrack(i+1)

            #with nums[i]
            s.append(nums[i])
            backtrack(i+1)
            s.pop()
        backtrack(0)
        return r