from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDic = defaultdict(list)
        finishedCourse = set()
        def dfs(i,visited):
            if i in finishedCourse:
                return True
            visited.add(i)
            prereq = courseDic[i]
            for pre in prereq:
                if len(courseDic[pre]) == 0:
                    finishedCourse.add(pre)
                elif pre in visited:
                    return False
                else:
                    if dfs(pre,visited) == False:
                        return False
            finishedCourse.add(i)
            return True

        for course  in prerequisites:
            courseDic[course[0]].append(course[1])
        for i in range(numCourses):
            visited = set()
            if dfs(i,visited) == False:
                return False
        return True
       

        


        