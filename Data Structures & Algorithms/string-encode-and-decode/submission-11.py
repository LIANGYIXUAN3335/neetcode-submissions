class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            cur = str(len(i)) + "#" + i
            res.append(cur)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        print(s)
        index = 0
        while index < len(s):
            curIndex = index
            while s[curIndex] != "#":
                curIndex += 1
            res.append(s[curIndex +1 : curIndex + 1 + int(s[index : curIndex])])
            index =  curIndex + 1 + int(s[index : curIndex])
        return res
