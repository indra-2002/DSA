class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n=len(nums)
        def houserobber(l):
            n=len(l)
           
            dp=[l[0],max(l[0],l[1])]
            for i in range(2,n):
                curr=max( dp[i-2] + l[i] , dp[i-1] )
                dp.append(curr)
            return dp[-1]
        if n==1 or n==2:
                return max(nums)
        return max(houserobber(nums[:-1]),houserobber(nums[1:]))

