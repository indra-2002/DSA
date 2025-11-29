class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1


        l=min(bloomDay)
        
        h=ans=max(bloomDay)
        while l<=h:
            mid=(l+h)//2
            count=0
            total=0
            for i in bloomDay:
                if i<=mid:
                    count+=1
                else:
                    total+=count//k
                    count=0
            total+=count//k

            if total>=m:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
            