class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        from collections import deque
        q=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[0][j]==1:
                    q.append((0,j))
                    grid[0][j]=0
                if grid[rows-1][j]==1:
                    q.append((rows-1,j))
                    grid[rows-1][j]=0
                if grid[i][0]==1:
                    q.append((i,0))
                    grid[i][0]=0
                if grid[i][cols-1]==1:
                    q.append((i,cols-1))
                    grid[i][cols-1]=0
        while q:
            r, c= q.popleft()
            for row,col in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc= row+r, col + c
                if 0<= nr < rows and 0 <=nc< cols and grid[nr][nc]==1:
                    grid[nr][nc]=0
                    q.append(( nr, nc))
                
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    count+=1
        return count