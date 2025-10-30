class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        def dfs(node,col):
            color[node]=col
            for i in graph[node]:
                if color[i]==-1:
                    if not dfs(i , 1- col):
                        return False
                elif color[i]==color[node]:
                    return False
            return True
        for i in range(n):
            if color[i]==-1:
                if not dfs(i,0):
                    return False
        return True
        
