from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1
        time=0
        while q:
            row,col,time=q.popleft()
            for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr=r+row
                nc=c+col
                if 0<= nr <  len(grid) and  0<= nc < len(grid[0]) and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc, time+1))
        return time if fresh == 0 else -1

