class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = {}
        for i in strs:
            curList = [0] * 26
            sortI = sorted(i)
            for j in sortI:
                curList[ord(j) - ord('a')] += 1
            if tuple(curList) not in strDict.keys():
                strDict[tuple(curList)] = []
            strDict[tuple(curList)].append(i)
        return strDict.values()
        