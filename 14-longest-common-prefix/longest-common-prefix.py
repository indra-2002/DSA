class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        f=strs[0]
        l=strs[-1]
        res=[]
        for i in range(len(min(f,l))):
            if f[i]==l[i]:
                res.append(f[i])
            else:
                break
        return "".join(res)
