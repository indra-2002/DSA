class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)> len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        n,m=len(nums1),len(nums2)
        l=0
        h=n
        while l<=h:
            mid1=(l+h)//2
            mid2=(n+m+1)//2 - mid1
            maxl1=float('-inf') if mid1==0 else nums1[mid1-1]
            minh1=float('inf') if mid1==n else nums1[mid1]

            maxl2=float('-inf') if mid2==0 else nums2[mid2 - 1]
            minh2=float('inf') if mid2==m else nums2[mid2]

            if maxl1 <= minh2 and maxl2 <= minh1:
                if (n+m)%2==0:
                    return (max(maxl1,maxl2)+ min(minh1,minh2))/2
                else:
                    return max(maxl1,maxl2)
            if maxl1> minh2:
                h=mid1-1
            else:
                l=mid1+1
        

