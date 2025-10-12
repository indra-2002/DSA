class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        unique=0
        for i in nums:
            unique^=i
        return unique