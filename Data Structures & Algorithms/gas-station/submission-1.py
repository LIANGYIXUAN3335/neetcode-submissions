class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return - 1
        n = len(gas)
        left = [0] * n
        for i in range(n):
            left[i] = gas[i] - cost[i]
        for start in range(n):
            if left[start] < 0:
                continue
            curLeft = left[start]
            for dis in range(1,n):
                curLeft += left[(start + dis) % n]
                if curLeft < 0:
                    break
            if curLeft >= 0:
                return start
        return -1