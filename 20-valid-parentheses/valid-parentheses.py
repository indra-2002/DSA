class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<2:
            return False
        stack =[]
        dic={')':'(','}':'{',']':'['}
        for i in s:
            if i not in dic:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    popped=stack.pop()
                    if popped !=dic[i]:
                        return False
        return not stack 

        