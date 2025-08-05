class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        d={}
        for i,v in enumerate(numbers):
            diff=target-v
            if diff in d:
                l.append(d[diff]+1)
                l.append(i+1)
            d[v]=i
        return l


