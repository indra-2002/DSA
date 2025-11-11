class disjoint:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[1]*n
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rooty==rootx:
            return 
        if self.size[rootx]> self.size[rooty]:
            self.parent[rooty]=rootx
            self.size[rootx]+=self.size[rooty]
        else:
            self.parent[rootx]=rooty
            self.size[rooty]+=self.size[rootx]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        
        ds=disjoint(n * n)
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    for r,c in directions:
                        nr,nc=r+i, c+j
                        if 0<=nr< n and 0<=nc<n and grid[nr][nc]==1:
                            ds.union(i*n + j , nr * n + nc)
        maxi=max(ds.size) if any(grid[i][j]==1 for i in range(n) for j in range(n)) else 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    unique_parent=set()
                    for r,c in directions:
                        nr,nc=r+i, c+j 
                        if 0<=nr <n and 0<=nc<n and grid[nr][nc]==1:
                            parent=ds.find(nr * n + nc)
                            unique_parent.add(parent)
                    
                    newsize=1
                    for parent in unique_parent:
                        size=ds.size[parent]
                        newsize+=size
                    maxi=max(maxi, newsize)
        return maxi



        