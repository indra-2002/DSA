class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                oprd1=stack.pop()
                oprd2=stack.pop()

                if i == '+':
                    
                    stack.append(oprd2+oprd1)
                elif i == '-':
                    
                    stack.append(oprd2-oprd1)
                elif i == '*':
                    
                    stack.append(oprd2*oprd1)
                else:
                    
                    stack.append(int(oprd2/oprd1))
        return stack[0]