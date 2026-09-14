class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        stack=[]    
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                a=int(stack.pop())
                b=int(stack.pop())
                if tokens[i] == '+':
                     c = b + a
                elif tokens[i] == '-':
                    c = b - a
                elif tokens[i] == '*':
                    c = b * a
                elif tokens[i] == '/':
                    c = int(b / a)
                stack.append(c)
            else:
                stack.append(int(tokens[i]))    
        return int(stack[-1])

