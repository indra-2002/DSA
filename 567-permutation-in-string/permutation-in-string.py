from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word=Counter(s1)
        if len(s1)> len(s2):
            return False
        per_count=Counter(s2[:len(s1)])
        if word== per_count:
            return True
        for i in range(len(s1),len(s2)):
            per_count[s2[i]]+=1
            per_count[s2[i-len(s1)]]-=1
            if per_count[s2[i-len(s1)]]==0:
                del per_count[s2[i-len(s1)]]
            if word==per_count:
                return True
        return False