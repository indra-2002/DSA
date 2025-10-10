from collections import deque,Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=Counter(tasks)
        maxheap=[-i for i in counter.values()]
        heapq.heapify(maxheap)
        time=0
        q=deque()

        while maxheap or q:
            time+=1
            if maxheap:
                popped=1+heapq.heappop(maxheap)
                if popped:
                    q.append((popped,time+n))
            if q and q[0][1]==time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time 