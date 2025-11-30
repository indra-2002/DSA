class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        h=sum(weights)
        ans=h
        while l<=h:
            mid=(l+h)//2
            total=0
            d=1
            for i in weights:
                if total+i <= mid:
                    total+=i
                else:
                    d+=1
                    total=i
            if d<=days:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
