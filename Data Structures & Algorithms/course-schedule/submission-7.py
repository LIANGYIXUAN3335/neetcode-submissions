class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # solution 1 use dfs to detect cycle
        requisiteMap = {i :[] for i in range(numCourses)}
        visiting = set()
        for courseMap in prerequisites:
            requisiteMap[courseMap[0]].append(courseMap[1])
        def dfs(course):
            if len(requisiteMap[course]) == 0:
                return True
            visiting.add(course)
            for i in requisiteMap[course]:
                if i in visiting:
                    return False
                if dfs(i) == False:
                    return False
            visiting.remove(course)
            requisiteMap[course] = []
            return True
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
