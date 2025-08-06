class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp=n
        rem=0
        s=0
        prod=1
        while temp!=0:
            rem=temp%10
            s+=rem
            prod*=rem
            temp/=10
        if n%(prod+s)==0:
            return bool(1)
        else:
            return bool(0)
