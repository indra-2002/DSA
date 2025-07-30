class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        r1=0
        l=0
        r=0
        for i in range(1,len(arr)-1):
            if arr[i-1]< arr[i] > arr[i+1]:
                l=i
                r=i
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                while r <len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                r1=max(r1,r-l+1)
        return r1