class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        approved = set()
        path = set()

        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        def dfs(course):
            if course in approved:
                return True

            if course in path:
                return False

            path.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            path.remove(course)
            approved.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True