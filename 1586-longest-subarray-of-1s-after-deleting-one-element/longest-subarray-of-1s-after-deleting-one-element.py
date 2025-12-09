class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        countzero=0
        l=0
        maxi=float('-inf')
        for r in range(len(nums)):
            if nums[r]==0:
                countzero+=1
            while l<r and countzero>1:
                if nums[l]==0:
                    countzero-=1
                l+=1
            maxi=max(r-l+1,maxi)
        return maxi-1
                    
               

            