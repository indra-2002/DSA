class Solution:
    def spanningTree(self, V, edges):
        # code here
        from collections import defaultdict
        import heapq
        graph=defaultdict(list)
        for i,j,k in edges:
            graph[i].append([j,k])
            graph[j].append([i,k])
            
        q=[]
        heapq.heapify(q)
        sum=0
        v=set()
        q.append((0,0,-1))
        while q:
            
            weight,node , parent= heapq.heappop(q)
            if node in v:
                continue
            sum+=weight
            v.add(node)
            for neigh, w in graph[node]:
                if neigh not in v:
                    heapq.heappush(q,(w,neigh,node))
        return sum
            