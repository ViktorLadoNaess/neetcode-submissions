class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops = {'+', '-', '*', '/'}

        for i in range(len(tokens)):
            if tokens[i] in ops:
                val2= int(stack.pop())
                val1= int(stack.pop())
                if tokens[i]=='+':
                    res= val1+val2
                elif tokens[i]=='*':
                    res = val1*val2
                elif tokens[i]=='-':
                    res = val1-val2
                else:
                    res = val1/val2
                stack.append(res)
            else:
                stack.append(tokens[i])
        return int(stack[0])

