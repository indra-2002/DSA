class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        sol=[]
        
        def backtrack(s):
            if len(sol)==k:

                res.append(sol[:])
                return
            for i in range(s,n+1):
                if i not in sol:
                    sol.append(i)
                    backtrack(i)
                    sol.pop()
        backtrack(1)
        return res
            