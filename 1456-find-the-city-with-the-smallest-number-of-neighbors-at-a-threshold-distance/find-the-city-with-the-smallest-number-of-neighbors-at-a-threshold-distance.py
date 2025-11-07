class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis=[[0 if i==j else float('inf')  for i in range(n)]for j in range(n)]
        for i,j,k in edges:
            dis[i][j]=k
            dis[j][i]=k

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dis[i][j]> dis[i][k] + dis[k][j]:
                        dis[i][j]=dis[i][k]+ dis[k][j]
        countmin=float('inf')
        city=-1
        
        for i in range(n):
            count=0
            for j in range(n):
                if dis[i][j] <= distanceThreshold:
                    count+=1
                
            if countmin>= count:
                countmin=count
                city=i
        return city