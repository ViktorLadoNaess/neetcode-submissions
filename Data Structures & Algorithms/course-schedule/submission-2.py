class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for i in prerequisites:
            graph[i[0]].append(i[1])
        print(graph)
        
        visiting= set()
        safe=set()
        def dfs(curr):
            if curr in safe:
                return True
            if curr in visiting:
                return False

            visiting.add(curr)
            for prereq in graph[curr]:
                if dfs(prereq)==False:
                    return False
            visiting.remove(curr)
            safe.add(curr)
            return True

        t = True
        for i in range(numCourses):
            t = dfs(i) and t
        return t
            