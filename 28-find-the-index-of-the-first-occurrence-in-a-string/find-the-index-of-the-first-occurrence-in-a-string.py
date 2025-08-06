class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a=0
        b=len(needle)

        while a<len(haystack):
            if haystack[a:a+b]==needle:
                return a
               
            else:
                a+=1
        return -1

        