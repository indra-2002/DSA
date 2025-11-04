#User function Template for python3

from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        from collections import deque
        q=deque()
        mod=100000
        dis=[float('inf')]*mod
        dis[start]=0
        q.append((0,start))
        while q :
            mult, number=q.popleft()
            if number==end:
                return mult
            for i in arr:
                n=(number*i)%mod
            
                if mult + 1 < dis[n]:
                    
                    dis[n]=mult+1
                    q.append((mult+1, n))
        return -1
                
                    