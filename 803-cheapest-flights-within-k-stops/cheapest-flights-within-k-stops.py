from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Min-heap: (cost, node, stops_used)
        heap = [(0, src, 0)]
        
        # Dictionary to store the minimum cost for (node, stops_used)
        best = {(src, 0): 0}
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            # If we reach the destination, return the cost (cheapest first due to heap)
            if node == dst:
                return cost
            
            # If we've used more than allowed stops, skip
            if stops > k:
                continue
            
            # Explore all neighbors
            for nei, price in graph[node]:
                new_cost = cost + price
                
                # Only push if this route is cheaper for the current (neighbor, stops + 1)
                if best.get((nei, stops + 1), float('inf')) > new_cost:
                    best[(nei, stops + 1)] = new_cost
                    heapq.heappush(heap, (new_cost, nei, stops + 1))
        
        # If destination not reachable within k stops
        return -1
