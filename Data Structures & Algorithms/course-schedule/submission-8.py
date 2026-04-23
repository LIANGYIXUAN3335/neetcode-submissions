# import deque from collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # solution 1 use dfs to detect cycle
        # requisiteMap = {i :[] for i in range(numCourses)}
        # visiting = set()
        # for courseMap in prerequisites:
        #     requisiteMap[courseMap[0]].append(courseMap[1])
        # def dfs(course):
        #     if len(requisiteMap[course]) == 0:
        #         return True
        #     visiting.add(course)
        #     for i in requisiteMap[course]:
        #         if i in visiting:
        #             return False
        #         if dfs(i) == False:
        #             return False
        #     visiting.remove(course)
        #     requisiteMap[course] = []
        #     return True
        # for course in range(numCourses):
        #     if dfs(course) == False:
        #         return False
        # return True
        # solution 2 topological sort
        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        for cur,pre in prerequisites:
            indegree[cur] += 1
            adj[pre].append(cur)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finished = 0
        while q:
            curCourse = q.popleft()
            finished += 1
            for i in (adj[curCourse]):
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return finished == numCourses
