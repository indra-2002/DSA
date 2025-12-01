class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def possible(position,dist):
            last=position[0]
            ball=1
            for i in range(len(position)):
                if position[i]-last>=dist:
                    ball+=1
                    last=position[i]
            if ball>=m:
                return True
            else:
                return False
        position.sort()
        l=1
        h=max(position)
        while l<=h:
            mid=(l+h)//2
            if possible(position,mid):
                l=mid+1
            else:
                h=mid-1
        return h