class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows= len(grid)
        cols=len(grid[0])
        island=0
        from collections import deque
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            grid[r][c]='0'
            while q:
                row1 , col1=q.popleft()
                for ver,hori in [(1,0),(-1,0),(0,1),(0,-1)]:
                    row= row1+ver 
                    col=col1+ hori
                    if 0<=row <rows and 0<= col<cols and grid[row][col]=='1':
                        grid[row][col]='0'
                        q.append((row,col))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    bfs(i,j)
                    island+=1
        return island