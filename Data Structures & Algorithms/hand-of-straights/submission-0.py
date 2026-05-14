from sortedcontainers import SortedDict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        countMap = SortedDict()
        for i in hand:
            countMap[i] = countMap.get(i, 0) + 1
        while countMap:
            cur = start = countMap.keys()[0]
            for _ in range(groupSize):
                
                if cur not in countMap:
                    return False
                else:
                    countMap[cur] -= 1
                    if countMap[cur] == 0:
                        del countMap[cur]
                cur += 1
        return True
        