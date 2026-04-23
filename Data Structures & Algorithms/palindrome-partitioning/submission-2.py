class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        memPal = [[False for _ in range(n)] for _ in range(n)]
        for length in range(n):
            for start in range(n - length):
                memPal[start][start + length] = (s[start] == s[start + length] and ( length <= 2 or memPal[start + 1][start + length - 1]))
        curList = []
        def dfs(index):
            if index == n:
                # res.append(curList.copy())
                return [[]]
            ret = []
            for i in range(index,n):
                if memPal[index][i]:
                    nxt = dfs(i + 1)
                    for part in nxt:
                        ret.append([s[index : i + 1]] + part )
            return ret
        return dfs(0)


        