class Solution:
    def isValid(self, s: str) -> bool:
        parentheseMap = {"]" : "[", "}" : "{" , ")" : "("}
        stack = []
        for i in s:
            if i in parentheseMap:
                if stack :
                    if stack[-1] != parentheseMap[i]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) ==0
            


        