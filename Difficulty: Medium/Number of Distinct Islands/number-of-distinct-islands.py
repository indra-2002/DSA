#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        rows = len(grid)
        cols=  len(grid[0])
        v=set()
        shapes=set()
        def dfs(r,c, baser, basec,shape):
            if r<0 or c< 0 or r>=rows or c>=cols or grid[r][c]==0 or (r,c) in v:
                return 
            
            v.add((r,c))
            shape.append((baser-r, basec- c))
            dfs(r+1,c,baser,basec,shape)
            dfs(r-1,c,baser,basec,shape)
            dfs(r,c+1,baser,basec,shape)
            dfs(r,c-1,baser,basec,shape)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in v:
                    shape=[]
                    dfs(i,j,i,j,shape)
                    shapes.add(tuple(shape))
        return len(shapes)