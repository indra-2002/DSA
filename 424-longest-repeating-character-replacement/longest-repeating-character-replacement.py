from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr=[0]*26
        l=0
        maxi=float('-inf')
        freq=0
        counter=Counter()
        for r in range(len(s)):
            idx=ord(s[r])-ord('A')
            counter[idx]+=1
            freq=max(freq,counter[idx])


            while (r-l+1)-freq>k:
                counter[ord(s[l])-ord('A')]-=1
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi



            