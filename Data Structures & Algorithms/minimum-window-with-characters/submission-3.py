class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ''
        tMap = {}
        for i in t:
            tMap[i] = tMap.get(i,0) + 1
        have = 0
        need = len(tMap)
        sMap = {}
        res = ''
        minLen = float("inf")
        left  = 0 
        for i in range(m):
            if s[i] in tMap:
                sMap[s[i]] = sMap.get(s[i],0) + 1
                if sMap[s[i]] == tMap[s[i]]:
                    have += 1
            if have == need:
                while s[left]  not in tMap or sMap[s[left]] > tMap[s[left]]:
                    if s[left]  not in tMap:
                        left += 1
                    elif sMap[s[left]] > tMap[s[left]]:
                        sMap[s[left]] -= 1
                        left += 1
                if i - left + 1 < minLen:
                    minLen = i - left + 1
                    res = s[left: i + 1 ]
        return res


        