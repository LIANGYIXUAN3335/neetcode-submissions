class Solution:

    def encode(self, strs: List[str]) -> str: 
        res = ''
        for i in strs:
            res += str(len(i))
            res += '#'
            res += i
        return res

    def decode(self, s: str) -> List[str]:
        index = 0
        res = []
        while index < len(s):
            r = index
            while r <len(s) and s[r] != "#":
                r += 1
            length = int(s[index:r])
            res.append(s[r+1:r+1+length ])
            index = r + length +1
        return res