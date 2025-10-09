from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        for i in range(len(tickets)):
            q.append((i,tickets[i]))
        time=0
        while q:
            index,ticket=q.popleft()
            ticket -= 1
            time += 1
            if  ticket > 0:
                q.append((index,ticket))
            if index==k and ticket==0:
                return time