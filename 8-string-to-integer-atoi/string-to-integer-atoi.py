class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s=s.lstrip()
        if not s:
            return 0
        sign=1
        i=0
        if s[i] in ["+","-"]:
            if s[i]=="-":
                sign=-1
            i+=1
        num=0
        while i<len(s) and s[i].isdigit():
            num=num*10+int(s[i])
            i+=1
        num*=sign
        
        mini=-2**31
        maxi=2**31-1

        if num<mini:
            return mini
        if num>maxi:
            return maxi
        return num