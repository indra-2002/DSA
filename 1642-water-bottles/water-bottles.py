class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        rem=0
        sum=numBottles
        while numBottles>=numExchange:
            res=numBottles//numExchange
            rem=numBottles%numExchange
            sum+=res
            numBottles=res+ rem
        return sum

        