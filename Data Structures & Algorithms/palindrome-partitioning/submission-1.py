class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        memPal = [[False for _ in range(n)] for _ in range(n)]
        for length in range(n):
            for start in range(n - length):
                memPal[start][start + length] = (s[start] == s[start + length] and ( length <= 2 or memPal[start + 1][start + length - 1]))
        curList = []
        print(memPal)
        res = []
        def dfs(index):
            print(index,curList)
            if index == n:
                res.append(curList.copy())
                return
            for i in range(index,n):
                if memPal[index][i] == True:
                    curList.append(s[index:i + 1])
                    dfs(i + 1)
                    curList.pop()
        dfs(0)
        return res


        