class Solution:
    def reverse(self, x: int) -> int:
        neg=1
        if x<0:
            neg=-1
        res=int(str(abs(x))[::-1]) * neg
        if res< -2**31-1 or res> 2**31-1:
            return 0
        return res


            
