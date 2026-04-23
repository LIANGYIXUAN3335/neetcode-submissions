class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            courseMap[i[0]].append(i[1])
        visiting = set()
        finished = set()
        res = []
        def dfs(course):
            if len(courseMap[course]) ==0:
                if course not in finished:
                    finished.add(course)
                    res.append(course)
                return True
            visiting.add(course)
            for i in courseMap[course]:
                if i in visiting:
                    return False
                if dfs(i) == False:
                    return False
            visiting.remove(course)
            courseMap[course] = []
            if course not in finished:
                finished.add(course)
                res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

        