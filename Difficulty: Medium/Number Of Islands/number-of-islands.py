#User function Template for python3

from typing import List
class disjoint:
    def __init__(self,n ):
        self.parent=[i for i in range(n)]
        self.size=[1]*n
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx==rooty:
            return
        if self.size[rooty]> self.size[rootx]:
            self.parent[rootx]=rooty
            self.size[rooty]+=self.size[rootx]
        else:
            self.parent[rooty]=rootx
            self.size[rootx]+=self.size[rooty]
            
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        ds=disjoint(rows*cols)
        islands=0
        v=[[0]*cols for _ in range(rows)]
        res=[]
        for i,j in operators:
            if v[i][j]==0:
                v[i][j]=1
                islands+=1
                for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+i, c+j
                    if 0<=nr < rows and 0<=nc < cols and v[nr][nc]==1:
                        if ds.find(i*cols + j) == ds.find( nr* cols + nc):
                            continue
                        ds.union(i*cols + j , nr* cols + nc)
                        islands-=1
                            
                res.append(islands)           
                            
            else: 
                res.append(islands)
                continue
                            
                            
                            
        return res
                            
                            
                            