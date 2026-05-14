class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}

        for t in tokens:
            if t not in ops:
                stack.append(int(t))  # ← cast string to integer
            else:
                b = stack.pop()
                a = stack.pop()

                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:  # '/'
                    stack.append(int(a / b))  # truncate toward 0

        return stack[0]