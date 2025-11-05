class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
        import heapq
        graph=defaultdict(list)
        for i, j, k in roads:
            graph[i].append([j, k ])
            graph[j].append([i, k ])
        ways=[0]*n
        dis=[float('inf')]*n
        dis[0]=0
        q=[]
        heapq.heapify(q)
        q.append((0,0))
        ways[0]=1
        while q:
            distance, node = heapq.heappop(q)
            
            if distance> dis[node]:
                continue
            for neigh , wiegh in graph[node]:
                
                if dis[neigh] > distance+ wiegh:
                    dis[neigh]=distance + wiegh
                    ways[neigh]=ways[node]
                    heapq.heappush(q,(dis[neigh],neigh))
                elif distance+ wiegh == dis[neigh]:
                    
                    ways[neigh]=(ways[neigh]+ways[node])
        return ways[n-1]%((10**9)+7)