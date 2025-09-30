class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r=[]
        for i in s:
            if i.isalnum():
                r.append(i.lower())
        s1="".join(r)
        s2="".join(r[::-1])
        if s1==s1[::-1]:
            return True
        return False
