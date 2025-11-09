class Disjoint:
    def __init__(self, n):
        self.parent=[i for i  in range(n)]
        self.rank=[0]*n
    def find(self,x):
        if self.parent[x]!= x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x, y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx== rooty:
            return 
        if self.rank[rooty]> self.rank[rootx]:
            self.parent[rootx]=rooty
        elif self.rank[rootx]  > self.rank[rooty]:
            self.parent[rooty]= rootx
        else:
            self.parent[rooty]=rootx
            self.rank[rootx]+=1
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        extraedge=0
        ds=Disjoint(n)
        for i,j in connections:
            if ds.find(i)==ds.find(j):
                extraedge+=1
            else:
                ds.union(i,j)
        count=0
        for i in range(n):
            if ds.parent[i]==i:
                count+=1
        if extraedge>= count-1:
            return count-1
        else:
            return -1
            
        