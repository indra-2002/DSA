
class Solution:
    def shortestPath(self, adj, src):
        # code here
        from collections import  deque
        
        dist=[float('inf')]*len(adj)
        q=deque([src])
        dist[src]=0
        while q:
            node=q.popleft()
            
            for neigh in adj[node]:
                if dist[neigh]> dist[node]+1:
                    dist[neigh]=dist[node]+1
                    q.append(neigh)
                
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist