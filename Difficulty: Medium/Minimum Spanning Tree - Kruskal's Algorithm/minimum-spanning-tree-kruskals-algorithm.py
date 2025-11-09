#User function Template for python3
from typing import List

class disjoint:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def find(self, x):
        if self.parent[x]==x:
            return self.parent[x]
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self, x,y):
        rootx= self.find(x)
        rooty=self.find(y)
        if rootx== rooty:
            return False
        if self.parent[rootx]> self.parent[rooty]:
            self.parent[rooty]=rootx
        elif self.parent[rooty]  > self.parent[ rootx]:
            self.parent[rootx]=rooty
        else:
            self.parent[rooty]=rootx
            self.rank[rooty]+=1
        return True
        
class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        
        # code here
        edges.sort(key=lambda x: x[2])
        weight=0
        ds=disjoint(V)
        for u,v, w in edges:
            if ds.union(u,v):
                weight+=w
        
        return weight