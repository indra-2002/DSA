class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m=0
        l=0
        r=1
        for r in range(len(prices)):
            if prices[l]<prices[r]:
                m=max(m,prices[r]-prices[l])
            else:
                l=r
                r+=1
        return m
            