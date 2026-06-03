class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+' ,'-' ,'*','/']:
                right = stack.pop()
                left = stack.pop()
                res = 0
                if token == "+":
                    res = left + right
                elif token == "-":
                    res = left - right
                elif token == "*":
                    res = left * right
                else:
                    res = int(left / right)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()
        