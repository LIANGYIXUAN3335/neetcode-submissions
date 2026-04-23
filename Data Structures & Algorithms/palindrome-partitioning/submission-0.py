class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        memPal = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            left = right = i
            while left >=0 and right < n:
                if s[left] == s[right] and (right - left <= 2 or memPal[left+ 1][right-1] == True):
                    memPal[left][right] = True
                left -= 1
                right += 1
        for i in range(n - 1):
            left, right = i , i + 1
            while left >=0 and right < n:
                if s[left] == s[right] and (right - left <= 2 or memPal[left+ 1][right-1] == True):
                    memPal[left][right] = True
                left -= 1
                right += 1 
        res = []
        curList = []
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


        