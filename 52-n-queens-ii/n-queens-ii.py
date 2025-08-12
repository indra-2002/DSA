class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col=set()
        posdiag=set()
        negdiag=set()
        
        result=[0]
        board=[["."]*n for _ in range(n)]

        def backtrack(r):
            
            if r==n:
                result[0]+=1
                return
            for c in range(n):
                if c in col or r+c in posdiag or r-c in negdiag:
                    continue
                
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                

                backtrack(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        backtrack(0)
        return result[0]