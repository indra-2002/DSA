class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        r=0
        m=len(s)
        if s== "":
            return True
        if len(s)> len(t):
            return False
        for i in range(len(t)):
            if t[i]== s[r]:
                m-=1
                r+=1
            if m==0:
                return True
        return False

