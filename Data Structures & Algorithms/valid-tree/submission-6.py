from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) !=n-1:
            return False
        
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])


        seen = set()
        def dfs(node):
            print(node)
            if node in seen:
                return 
            seen.add(node)
            for n in graph[node]:
                dfs(n)
        dfs(0)
        return len(seen) == n

        
