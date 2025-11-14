class Solution:

    def kosaraju(self, adj):
        #code here
        def dfs(node):
            v.add(node)
            for i in adj[node]:
                if i not in v:
                    
                    dfs(i)
            stack.append(node)
        from collections import defaultdict
        graph=defaultdict(list)
        stack=[]   
        v=set()
        count=0
        for i in range(len(adj)):
            if i not in v:
                dfs(i)
        for i in range(len(adj)):
            for j in adj[i]:
                graph[j].append(i)
        v=set()
        def dfs2(node):
            v.add(node)
            for i in graph[node]:
                if i not in v:
                    dfs2(i)
        while stack:
            x=stack.pop()
            if x not in v:
                dfs2(x)
                count+=1
        return count
        
        
        
        
        
        