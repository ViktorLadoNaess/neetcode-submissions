class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        approved = set()
        path = set()

        preMap = {i: [] for i in range(numCourses)}
        for c,r in prerequisites:
            preMap[c].append(r)

        def dfs(course):
            if course in approved:
                return True
            if course in path:
                return False
            
            path.add(course) 
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
                
            path.remove(course)
            approved.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            



