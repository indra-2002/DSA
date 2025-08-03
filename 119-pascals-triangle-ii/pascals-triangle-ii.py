class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n=[]
        for i in range(rowIndex+1):
            r=[1]*(i+1)
            for j in range(1,i):
                r[j]=n[i-1][j]+n[i-1][j-1]
            n.append(r)
        return n[rowIndex]