from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need=Counter(t)
        left=start=end=0
        window=Counter()
        missing=len(t)
        for right,char in enumerate(s):
            
            window[char]+=1
            if need[char]>= window[char]:

                missing-=1
            while missing==0:
                if end == 0 or right+1 - left < end - start:
                    start,end = left , right+1
                window[s[left]]-=1
                if need[s[left]]> window [s[left]]:
                    missing+=1
                left+=1
                
        return s[start:end]