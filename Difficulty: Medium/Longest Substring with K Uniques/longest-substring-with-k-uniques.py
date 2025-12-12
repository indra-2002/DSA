from collections import Counter
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        l=0
        if len(Counter(s))<k:
            return -1
        count={}
        maxi=float('-inf')
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]]=1
            else:
                count[s[i]]+=1
            while len(count)>k:
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1
            maxi=max(maxi,i-l+1)
        return maxi
                