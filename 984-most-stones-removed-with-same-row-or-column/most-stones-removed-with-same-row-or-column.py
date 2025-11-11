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
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        ds=disjoint(n)
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    ds.union(i,j)
        unique_parents=set()
        for i in range(n):
            unique_parents.add(ds.find(i))
        return n - len(unique_parents)
            