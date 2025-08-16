class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        s=str(num)
        s=list(s)
        for i in range(len(s)):
            if s[i]=='6':
                s[i]='9'
                break
        return int("".join(s))    