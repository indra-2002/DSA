class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=set()
        once=set()
        for i in range(len(s)-9):
            if s[i:i+10] in once:
                result.add(s[i:i+10])
            else: 
                once.add(s[i:i+10])
        return list(result)
