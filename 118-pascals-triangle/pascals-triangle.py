class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n=[]
        for i in range(numRows):
            r=[1]*(i+1)
            for j in range(1,i):
                r[j]=n[i-1][j]+n[i-1][j-1]
            n.append(r)
        return n
            


