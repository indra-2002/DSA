#User function Template for python3
from typing import List
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        import heapq
        from collections import defaultdict
        graph=defaultdict(list)
        for i,j,k in edges:
            graph[i].append([j,k])
            graph[j].append([i,k])
        minq=[]
        heapq.heapify(minq)
        dis=[float('inf')]*(n+1)
        parent=[i for i in range(n+1)]
        dis[1]=0
        heapq.heappush(minq,(0,1))
        while minq:
            distance, vertex=heapq.heappop(minq)
            for neigh, wigh in graph[vertex]:
                if dis[neigh]> dis[vertex]+wigh:
                    dis[neigh]=dis[vertex]+wigh
                    parent[neigh]=vertex
                    heapq.heappush(minq,(dis[neigh],neigh))
        if dis[n]== float('inf'):
            return [-1]
        node=n
        res=[]
        while parent[node]!= node:
            res.append(node)
            node= parent[node]
        res.append(1)
        res.reverse
        return [dis[n]] +res
        