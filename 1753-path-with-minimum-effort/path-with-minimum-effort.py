class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import heapq
        rows, cols = len(heights), len(heights[0])
        dis=[[float('inf')]*cols for _ in range(rows)]
        dis[0][0]=0
        minq=[]
        heapq.heapify(minq)
        minq.append((0,0,0))
        while minq:
            distance, row, col = heapq.heappop(minq)
            if row== rows-1 and col == cols-1:
                return distance
            if distance> dis[row][col]:
                continue
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc= row+i, col + j
                if 0<= nr < rows and 0<= nc < cols:
                    max_distance=max(distance,abs(heights[nr][nc]-heights[row][col]))
                    if dis[nr][nc] > max_distance:
                        dis[nr][nc]= max_distance
                        heapq.heappush(minq,(dis[nr][nc],nr , nc))
        return 0