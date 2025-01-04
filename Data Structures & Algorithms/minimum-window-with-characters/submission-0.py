class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, tCount = {},{}
        res, resLen = [-1,-1] , float('infinity')
        for i in t:
            tCount[i] = tCount.get(i,0) + 1
        need, have = len(tCount), 0
        left =0
        for right in range(len(s)):
            if s[right] in tCount:
                window[s[right]] =window.get(s[right] , 0) + 1
                if window[s[right]] == tCount[s[right]]:
                    have += 1
            if need == have:
                while need == have:
                    if (right - left + 1) < resLen:
                        res = [left ,right ]
                        resLen = right - left +1
                    if s[left] in tCount:
                        if window[s[left]] == tCount[s[left]]:
                            have -= 1
                        window[s[left]] -= 1
                    left += 1

        l,r = res
        return s[l : r+1] if resLen != float("infinity") else ""

        