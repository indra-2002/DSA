class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        import heapq
        from collections import defaultdict
        graph=defaultdict(list)
        for i,j,k in edges:
            graph[i].append([j,k])
            graph[j].append([i,k])
        dis=[float('inf')]*V
        dis[src]=0
        minq=[]
        heapq.heapify(minq)
        minq.append((0,src))
        while minq:
            distance, vertex=heapq.heappop(minq)
            for neigh,wigh in graph[vertex]:
                if dis[neigh]>dis[vertex]+wigh:
                    dis[neigh]=dis[vertex]+wigh
                    heapq.heappush(minq,((dis[neigh],neigh)))
        return dis