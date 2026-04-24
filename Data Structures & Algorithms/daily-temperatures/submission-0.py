class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexList = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while indexList and temperatures[i] > temperatures[indexList[-1]]:
                res[indexList[-1]] = i - indexList[-1]
                indexList.pop()
            indexList.append(i)
        return res

        