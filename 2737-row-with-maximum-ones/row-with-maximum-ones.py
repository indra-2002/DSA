class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        '''def count(arr):
            l=0
            h=len(arr)-1
            ans=len(arr)
            while l<=h:
                mid=(l+h)//2
                if arr[mid]==1:
                    ans=mid
                    h=mid-1
                else:
                    l=mid+1
            return ans
        
        maxi=float('-inf')
        index=0
        for i in range(len(mat)):
            c=len(mat[i])-count(mat[i]) 
            if c > maxi:
                maxi=c
                index=i
        return [index,maxi]'''
        count=0
        maxi=-1
        idex=0
        for i,val in enumerate(mat):
            count=sum(val)
            if count> maxi:
                maxi=count
                idex=i
        return [idex,maxi]