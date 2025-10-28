class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols=len(mat),len(mat[0])
        dis=[[float('inf')]* cols for _ in range(rows)]
        from collections import deque
        q=deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    dis[i][j]=0
                    q.append((i,j))
        while q:
            row, col= q.popleft()
            for r, c in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+row,col+c
                if 0<= nr < rows and 0<= nc < cols and dis[nr][nc]> dis[row][col]+1:
                     dis[nr][nc] = dis[row][col]+1
                     q.append((nr, nc))
        return dis
