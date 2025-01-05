from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for string in strs:
            curMap = [0] * 26
            for ch in string:
                curMap[ord(ch) - ord("a")] += 1
            anagramMap[tuple(curMap)].append(string)
        return list(anagramMap.values())
        