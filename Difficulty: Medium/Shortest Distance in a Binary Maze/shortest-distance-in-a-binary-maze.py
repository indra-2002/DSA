#User function Template for python3

from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        n=len(grid)
        m=len(grid[0])
        if source==destination:
            return 0
        dis=[[float('inf')]*m for _ in range(n)]
        dis[source[0]][source[1]]=0
        from collections import deque
        q=deque()
        q.append((0,source[0],source[1]))
        while q:
            distance, row, col = q.popleft()
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc= row+ i, col + j
                if 0<=nr< n and  0<=nc<m and grid[nr][nc]==1:
                    if dis[nr][nc]>distance+1:
                        
                        dis[nr][nc]=distance+1
                        if nr==destination[0] and nc== destination[1]:
                            return distance+1
                    
                        q.append((distance+1,nr,nc))
        return -1