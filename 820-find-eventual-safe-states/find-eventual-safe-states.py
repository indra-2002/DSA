class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''n=len(graph)
        path=[0]*n
        safe=[0]*n
        v=[0]*n
        def dfs(node):
            v[node]=1
            path[node]=1
            for neig in graph[node]:
                if v[neig]==0:
                    if not dfs(neig):
                        return False
                elif path[neig]==v[neig]:
                    return False
            path[node]=0
            safe[node]=1
            return True
        for i in range(n):
            if v[i]==0:
                dfs(i)
        ans=[i for i in range(n) if safe[i]==1 ]
        return ans'''
        from collections import defaultdict, deque
        rev_graph=defaultdict(list)
        n=len(graph)
        indegree=[0]*n
        q=deque()
        for i in range(n):
            for j in graph[i]:
                rev_graph[j].append(i)
                indegree[i]+=1
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for neig in rev_graph[node]:
                indegree[neig]-=1
                if indegree[neig]==0:
                    q.append(neig)
        return sorted(res)