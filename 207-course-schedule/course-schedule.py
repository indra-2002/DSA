class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        graph=defaultdict(list)
        for c,p in prerequisites:
            graph[p].append(c)
        
        v=[0]*numCourses
        path=[0]*numCourses
        def dfs(node):
            v[node]=1
            path[node]=1
            for neig in graph[node]:
                if v[neig]==0:
                    if not dfs(neig):
                        return False
                elif v[neig]==path[neig]:
                    return False
            path[node]=0
            return True

        for i in range(numCourses):
            if v[i]==0:
                if not dfs(i):
                    return False
        return True

