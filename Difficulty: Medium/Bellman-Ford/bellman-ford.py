#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        dis=[10**8]*V
        dis[src]=0
        for _ in range(V-1):
            for i,j,k in edges:
                if dis[i]!= 10**8 and dis[i]+k < dis[j] :
                    dis[j]=dis[i]+k
        
        for i,j,k in edges:
            if dis[i]!= 10**8 and dis[i]+k < dis[j] :
                
                return [-1]
        return dis