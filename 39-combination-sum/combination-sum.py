class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        sol=[]
        def backtrack(start):
            if sum(sol)==target:
                res.append(sol[:])
                return 
            for i in range(start,len(candidates)):
                sol.append(candidates[i])
                if sum(sol)>target:
                    sol.pop()
                    continue

                backtrack(i)
                sol.pop()
        backtrack(0)
        return res
