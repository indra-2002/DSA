class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        import heapq
        heap=[]
        counter=Counter(words)
        for key , val in counter.items():
            
                heapq.heappush(heap,(-val,key))
            
        
        result = [ heapq.heappop(heap)[1] for _ in range(k)]
        return result

