class Solution:
    def isValid(self, s: str) -> bool:
        charStack = []
        charMap = {"{" : "}" , "(" : ")" , "[" : "]"}
        for i in s:
            if i in charMap.keys():
                charStack.append(i)
            elif len(charStack) == 0:
                return False
            else:
                lastClose = charStack.pop()
                if  i != charMap[lastClose]:
                    return False
        return len(charStack) == 0
        