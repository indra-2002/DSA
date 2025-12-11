from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(p)
        if n > len(s):
            return []
        p_count=Counter(p)
        s_count=Counter(s[:n])
        res=[]
        if p_count==s_count:
            res.append(0)
        for i in range(n,len(s)):
            s_count[s[i]]+=1
            s_count[s[i-n]]-=1
            if s_count[s[i-n]]==0:
                del s_count[s[i-n]]
            if s_count==p_count:
                res.append(i-n+1)
        return res