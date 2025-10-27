class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        province=0
        v=set()
        def dfs(i):
            for j in range(n):
                if isConnected[i][j]==1 and j not in v:
                    v.add(j)
                    dfs(j)


        for i in range(n):
            if i not in v:
                dfs(i)
                province+=1
        return province