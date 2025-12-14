class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        presum=0
        count=0
        for i in range(len(nums)):
            presum+=nums[i]
            s=presum-k
            if s in dic:
                count+=dic[s]
            if presum not in dic:
                dic[presum]=1
            else:
                dic[presum]+=1
            
        return count
