class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        def expand(l, r):
            nonlocal res
            if r < n and s[l] == s[r]:
                while l >= 0 and r < n and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return res