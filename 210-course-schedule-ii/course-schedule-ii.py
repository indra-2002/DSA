class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        from collections import defaultdict,deque
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for neig in graph[node]:
                indegree[neig]-=1
                if indegree[neig]==0:
                    q.append(neig)
        return res if len(res)==numCourses else []

        