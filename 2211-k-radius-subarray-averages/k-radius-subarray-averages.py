class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        res=[-1]*len(nums)
        window=2*k+1
        if window>len(nums):
            return res
        windowsum=sum(nums[:window])

        res[k]=windowsum//window
        l=0
        for r in range(window,len(nums)):
            windowsum+=nums[r]
            windowsum-=nums[l]
            l+=1
            index=l+k
            res[index]=windowsum//window
        return res 