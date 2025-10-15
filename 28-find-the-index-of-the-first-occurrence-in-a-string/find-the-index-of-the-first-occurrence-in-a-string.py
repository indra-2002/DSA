class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps=[0]*len(needle)
        i=1
        prevlps=0
        
        while i < len(needle):
            
            if needle[i]==needle[prevlps]:
                lps[i]=prevlps + 1
            
                prevlps+=1
                i+=1
            elif prevlps==0:
                lps[i]=0
                i+=1
            else:
                prevlps=lps[prevlps - 1]
        i=j=0
        while i < len(haystack):
            if haystack[i]==needle [j]:
                i+=1
                j+=1
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]

            if j==len(needle):
                return i-j
        return -1
