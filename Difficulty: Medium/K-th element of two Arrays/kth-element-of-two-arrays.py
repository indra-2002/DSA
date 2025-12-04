class Solution:
    def kthElement(self, a, b, k):
        # code here
        if len(a)>len(b):
            return self.kthElement(b,a,k)
        l=max(0,k-len(b))
        h=min(k,len(a))
        while l<=h:
            m1=(l+h)//2
            m2=k- m1
            l1=float('-inf') if m1==0 else a[m1-1]
            h1=float('inf') if m1==len(a) else a[m1]
            
            l2=float('-inf') if m2==0 else b[m2-1]
            h2=float('inf') if m2==len(b) else b[m2]
            
            if l1<= h2 and l2<= h1:
                return max(l1,l2)
            if l1> h2:
                h=m1-1
            else:
                l=m1+1
            
                