from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for start in sorted(count):
            if count[start] > 0:
                freq = count[start]

                for x in range(start, start + groupSize):
                    if count[x] < freq:
                        return False
                    count[x] -= freq

        return True