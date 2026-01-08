class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        r=len(grid)
        c=len(grid[0])
        v=[[0]*c for _ in range(r)]
        def dfs(row,col,pr,pc,ch):
            if v[row][col]==1:
                return True
            v[row][col]=1
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr=row+i
                nc=col+j
                if 0<=nr<r and 0<=nc<c and grid[nr][nc]==ch:
                    if (nr,nc) == (pr,pc):
                        continue
                    if dfs(nr,nc,row,col,ch):
                        return True
            return False
        for i in range(r):
            for j in range(c):
                if not v[i][j]:
                    if dfs(i,j,-1,-1,grid[i][j]):
                        return True
        return False