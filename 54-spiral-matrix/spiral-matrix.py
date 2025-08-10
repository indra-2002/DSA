class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r=[]
        while matrix:
            r+=(matrix.pop(0))
            if matrix and matrix[0]:
                for j in matrix:
                    r.append(j.pop())
            if matrix:
                r+=(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for j in matrix[::-1]:
                    r.append(j.pop(0))
        return r