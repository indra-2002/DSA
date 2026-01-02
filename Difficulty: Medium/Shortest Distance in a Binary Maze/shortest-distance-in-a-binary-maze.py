#User function Template for python3

from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        row=len(grid)
        col=len(grid[0])
        if source==destination:
            return 0
        dis=[[float("inf")]*col for _ in range(row)]
        dis[source[0]][source[1]]=0
        from collections import deque
        q=deque()
        q.append((0,source[0],source[1]))
        while q:
            distance,r,c=q.popleft()
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+i,c+j
                if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                    if distance+1< dis[nr][nc]:
                        dis[nr][nc]=distance+1
                        
                        if [nr,nc]==destination:
                            return distance+1
                        q.append((dis[nr][nc],nr,nc))
        return -1
                    