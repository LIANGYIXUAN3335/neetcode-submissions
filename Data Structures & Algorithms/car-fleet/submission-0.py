class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carList = []
        for i in range(len(position)):
            carList.append((position[i], speed[i]))
        carList.sort(key = lambda x : x[0])
        preTime = 0
        res = 0
        for i in range(len(position) - 1 , -1, -1):
            pos, spe = carList[i]
            curTime = (target - pos) / spe
            if curTime > preTime:
                res += 1
                preTime = curTime
        return res
