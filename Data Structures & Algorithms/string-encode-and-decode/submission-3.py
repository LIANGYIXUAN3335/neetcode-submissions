class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i))
            res += '#'
            res += i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # 找到下一个 '#'，用于确定长度部分的结尾
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end  # 推进到下一个编码起点
        return res

