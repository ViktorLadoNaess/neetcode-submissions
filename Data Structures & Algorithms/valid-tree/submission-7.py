from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen =set()
        def dfs(node):
            if node in seen:
                return 
            else:
                seen.add(node)
                for nei in graph[node]:
                    dfs(nei)
            return
        print(dfs(0))
        print(seen)
        
        return len(seen)== n

            