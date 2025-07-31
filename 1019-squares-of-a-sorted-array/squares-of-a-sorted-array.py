class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r1=[]
        l=0
        r=len(nums)-1
        while l<=r:
            leftvalue=abs(nums[l])
            rightvalue=abs(nums[r])

            if leftvalue > rightvalue:
                r1.append(leftvalue*leftvalue)
                l+=1
            else:
                r1.append(rightvalue*rightvalue)
                r-=1

        return r1[::-1]