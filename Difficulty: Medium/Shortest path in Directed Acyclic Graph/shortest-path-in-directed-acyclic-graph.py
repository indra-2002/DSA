#User function Template for python3

from typing import List


class Solution:


    def shortestPath(self, v: int, E: int,edges: List[List[int]]) -> List[int]:
        from collections import deque, defaultdict
        graph= defaultdict(list)
        vi=[False]*v
        dist=[float('inf')]*v
        stack=[]
        for i,j,k in edges:
            graph[i].append((j,k))
        def dfs(node):
            vi[node]=True
            for neigh,_ in graph[node]:
                if not vi[neigh]:
                    dfs(neigh)
            stack.append(node)
        for i in range(v):
            if not vi[i]:
                dfs(i)
        dist[0]=0
        for i in stack[::-1]:
            if dist[i]!=float('inf'):
                for neigh,wigh in graph[i]:
                    if dist[neigh] > dist[i]+wigh:
                        dist[neigh] = dist[i]+wigh
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist
                        
                        
            