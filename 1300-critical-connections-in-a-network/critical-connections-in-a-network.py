class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph=[[] for _ in range(n)] 
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        dis=[-1]*n
        lowest=[0]*n
        
        time =0 
        bridges=[]
        def dfs( node, parent):
            nonlocal time
            dis[node]=lowest[node]=time
            time+=1
            for neigh in graph[node]:
                if  neigh == parent:
                    continue
                if dis[neigh]==-1:
                    dfs(neigh,node)
                    lowest[node]=min(lowest[neigh], lowest[node])
                    if lowest[neigh] > dis[node]:
                        bridges.append((node, neigh))
                else:
                    lowest[node]=min(lowest[node],dis[neigh])
        for i in range(n):
            if dis[i]==-1:
                dfs(i,-1)
        return bridges
