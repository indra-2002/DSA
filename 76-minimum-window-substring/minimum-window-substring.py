from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        left=start=end=0
        missing=len(t)
        word=Counter()
        
        for index,val in enumerate(s):
            word[val]+=1
            if word[val]<=need[val]:
                missing-=1
            while missing==0:
                if end == 0 or index+1 - left < end-start:
                    start,end=left,index+1
                word[s[left]]-=1
                if need[s[left]]>word[s[left]]:
                    missing+=1
                left+=1
           
        return s[start:end]