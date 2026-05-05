class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        fromTo = [[] for _ in range(numCourses)]
        res = []
        for to , fro in prerequisites:
            fromTo[fro].append(to)
            inDegree[to] += 1
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            curCourse = q.popleft()
            res.append(curCourse)
            for course in fromTo[curCourse]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    q.append(course)
        return res if len(res) == numCourses else []