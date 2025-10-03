class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return - 1
        n = len(gas)
        tank = 0
        curStop = 0
        start = curStop
        while curStop < 2 * n:
            tank += gas[curStop % n] - cost[curStop % n]
            curStop += 1
            if tank < 0:
                start = curStop
                tank = 0
        
        return start