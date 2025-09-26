class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1 or n==2: return max(nums)

        dp=[nums[0],max(nums[0],nums[1])]
        for i in range(2,n):
            cur=max(nums[i]+dp[i-2],dp[i-1])
            dp.append(cur)
        return dp[-1]
        