class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s=set()
        for i ,v in enumerate(nums):
            if v in s:
                return bool(1)
            s.add(v)
            if len(s)>k:
                s.remove(nums[i-k])
        return bool(0)