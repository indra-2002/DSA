class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triple=set()
        
        for i,v in enumerate(nums):
            if i<0 & v==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                cs=v+nums[l]+nums[r]
                if cs>0:
                    r-=1
                elif cs<0:
                    l+=1
                else:
                    t=(v,nums[l],nums[r])
                    triple.add(t)
                    l+=1
                    
                    
                    
                      
        return [list(i) for i in triple]
            

                        

            
            