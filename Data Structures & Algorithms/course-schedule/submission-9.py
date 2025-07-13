class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        fromTo = [[] for _ in range(numCourses)]
        finished = 0
        for fro , to in prerequisites:
            fromTo[fro].append(to)
            inDegree[to] += 1
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            curCourse = q.popleft()
            finished += 1
            for course in fromTo[curCourse]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    q.append(course)
        return finished == numCourses
                

        