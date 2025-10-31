class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        from collections import defaultdict
        graph=defaultdict(list)
        for i,j in prerequisites:
            graph[j].append(i)
        v=[0]*numCourses
        path=[0]*numCourses
        stack=[]
        def dfs(node):
            v[node]=1
            path[node]=1
            for neigh in graph[node]:
                if v[neigh]==0:
                    if not dfs(neigh):
                        return False
                elif path[neigh]==1:
                    return False
            path[node]=0
        
            stack.append(node)
            return True


        for i in range(numCourses):
            if v[i]==0:
                if not dfs(i):
                    return []
        return stack[::-1]