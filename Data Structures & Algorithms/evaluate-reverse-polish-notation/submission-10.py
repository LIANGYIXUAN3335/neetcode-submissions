import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        # 将运算符直接映射为具体的操作函数，消除 if-elif 分支
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            # 用 lambda 保证在 Python 中实现向零截断的整数除法
            "/": lambda l, r: int(l / r) 
        }
        
        for token in tokens:
            if token in ops:
                right = stack.pop()
                left = stack.pop()
                # 直接从字典里取函数并执行
                stack.append(ops[token](left, right))
            else:
                stack.append(int(token))
                
        return stack.pop()