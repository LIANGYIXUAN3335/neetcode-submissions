class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calStack = []
        operator = ['+','-','*' ,'/']
        for i in range(len(tokens)):
            if tokens[i] in operator:
                num1 = (calStack.pop())
                num2 = (calStack.pop())
                if tokens[i] == "+":
                    curRes = num1 + num2
                elif tokens[i] == "-":
                    curRes = num2 -  num1
                elif tokens[i] == "*" :
                    curRes = num1 * num2
                else:
                    curRes = int(float(num2) / num1)
                calStack.append(curRes)
            else:
                calStack.append(eval(tokens[i]))
        return calStack[-1]

