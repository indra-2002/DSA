class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq
        heap=[]
        for i,j in points:
            distance = -(i*i + j*j)
            if len(heap)==k:

                heapq.heappushpop(heap,(distance,i,j))
            else:
                heapq.heappush(heap,(distance,i,j))
        return [[i,j] for (dist,i,j) in heap]

