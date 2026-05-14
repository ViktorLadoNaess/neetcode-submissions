class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in op.keys():
                if len(stack) == 0:
                    return False
                if op[i] == stack[-1]:
                    stack.pop()
                else: return False
            else:
                stack.append(i)
        if len(stack) != 0:
            return False
        return True
            
                