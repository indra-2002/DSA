#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        dis=[-1]*V
        lowest=[0]*V
       
        ap=[False]*V
        time=0
        def dfs(node, parent):
            nonlocal time
            dis[node]=lowest[node]=time
            time+=1
            children=0
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if dis[neigh]==-1:
                    children+=1
                    dfs(neigh,node)
                    lowest[node]=min(lowest[node],lowest[neigh])
                    if parent!= -1 and lowest[neigh] >= dis[node]:
                        ap[node]=True
                else:
                    lowest[node]=min(lowest[node], dis[neigh])
                    
            if parent==-1 and children> 1:
                ap[node]=True
        for i in range(V):
            if dis[i]==-1:
                dfs(i,-1)
        result=[ i for i in range(V) if ap[i]]
        return result if result else [-1]
            