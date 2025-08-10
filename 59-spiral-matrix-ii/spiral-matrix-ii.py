class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        r=[[0] * n for _ in range(n)]
        num=1
        left=0
        right=n-1
        top=0
        bottom=n-1
        while left<=right and top <= bottom:
            for col in range(left , right + 1):
                r[top][col]=num
                num+=1
            top+=1
            for row in range(top, bottom+1):
                r[row][right]=num
                num+=1
            right-=1
            if top <=bottom:

                for col in range(right,left-1,-1):
                    r[bottom][col]=num
                    num+=1
                bottom-=1
            if left<=right:
                for row in range(bottom,top-1,-1):
                    r[row][left]=num
                    num+=1
                left+=1
        return [i for i in r]
