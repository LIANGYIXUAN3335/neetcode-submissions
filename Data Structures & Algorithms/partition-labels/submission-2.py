class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charMap = {}
        n = len(s)
        for i in range(n):
            if s[i] in charMap:
                charMap[s[i]][1] = i
            else:
                charMap[s[i]] = [i,i]
        intervals= list(charMap.values())
        intervals.sort(key = lambda x : x[0])
        resLen = [intervals[0]]
        for interval in intervals:
            if interval[0] > resLen[-1][1]:
                resLen.append(interval)
            else:
                resLen[-1][1] = max(interval[1], resLen[-1][1])
        res = []
        for start, end in resLen:
            res.append(end - start + 1)
        return res





        