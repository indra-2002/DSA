import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter=Counter(nums)
        heap=[]

        for key,v in counter.items():
            if len(heap)<k:
                heapq.heappush(heap,(v,key))
            else:
                heapq.heappushpop(heap,(v,key))
        return [h[1]  for h in heap]