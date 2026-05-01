class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = [0] * 26
        for task in tasks:
            taskMap[ord(task) - ord('A')] += 1
        taskMap.sort(reverse = True)
        taskCount = 0
        res = 0
        while taskCount < len(tasks):
            curLen = 0
            taskMap.sort(reverse = True)
            for i in range(26):
                if curLen > n:
                    break
                if taskMap[i] > 0:
                    taskMap[i] -= 1
                    res +=  1
                    curLen += 1
                    taskCount += 1
            if taskCount < len(tasks) and n - curLen + 1 > 0:
                res += n - curLen + 1
        return res  