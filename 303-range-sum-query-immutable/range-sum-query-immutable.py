class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.r=[0]
        for i in nums:
            self.r.append(self.r[-1]+i)

        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.r[right+1]-self.r[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)