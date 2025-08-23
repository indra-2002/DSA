class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output=[""]
        for i in s:
            temp=[]
            if i.isalpha():
                for o in output:
                    temp.append(o+i.lower())
                    temp.append(o+i.upper())
            else:
                for o in output:
                    temp.append(o+i)
            output=temp
        return output
