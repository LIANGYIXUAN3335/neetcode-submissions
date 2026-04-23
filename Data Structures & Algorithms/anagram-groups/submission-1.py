from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)
        for i in strs:
            strMap[tuple(sorted(list(i)))].append(i)
        return strMap.values()
        