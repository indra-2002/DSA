class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m=0
        high=prices[0]
        low=prices[0]
        i=0
        while i< len(prices)-1:
            while i<len(prices)-1 and prices[i]>=prices[i+1]:
                i+=1
            low=prices[i]
            while i<len(prices)-1 and prices[i]<=prices[i+1]:
                i+=1
            high=prices[i]
            m+=high-low
        return m