class Solution:
    def nthRoot(self, n, m):
       # code here
        l=0
        h=m
        
        while l<=h:
            
            mid=(l+h)//2
            if mid**n ==m:
                return mid
            elif (mid**n) <m:
               
               l=mid+1
            else:
                h=mid-1
        return -1
       
