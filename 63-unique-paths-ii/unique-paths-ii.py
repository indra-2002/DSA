class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        
        if obstacleGrid[0][0]==1 or  obstacleGrid[m-1][n-1]==1:
            return 0
        board=[[0]*n for _ in range(m)]
        board[0][0]=1
        for i in range(m):
            for j in range(n):
                
                if obstacleGrid[i][j]==1:
                    board[i][j]=0
                else:
                    if i>0:
                        board[i][j]+=board[i-1][j]
                    if j>0:
                        board[i][j]+=board[i][j-1]
         
        return board[m-1][n-1]