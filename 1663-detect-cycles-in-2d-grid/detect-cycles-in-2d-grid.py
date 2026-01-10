class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        v=[[0]*m for _ in range(n)]
        def dfs(r,c,pr,pc,ch):
            if v[r][c]==1:
                return True
            v[r][c]=1
            for row,col in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=row+r,col+c
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==ch:
                    
                    if (nr,nc)==(pr,pc):
                        continue
                    if dfs(nr,nc,r,c,ch):
                        return True
        for i in range(n):
            for j in range(m):
                if v[i][j]==0:
                    if dfs(i,j,-1,-1,grid[i][j]):
                        return True
        return False

            