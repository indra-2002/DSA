class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def plandrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        ans=[]
        sol=[]
        def backtrack(start):
            if start==len(s):
                ans.append(sol[:])
                return 

            for i in range(start,len(s)):
                if plandrome(start,i):
                    sol.append(s[start:i+1])
                    backtrack(i+1)
                    sol.pop()
                
        backtrack(0)
        return ans 

        