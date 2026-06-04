class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            else: 
                seen.add(node)
            for c in graph[node]:
                dfs(c)
                
        res=0
            
        for i in graph:
            if i not in seen:
                res +=1
                dfs(i)
        return res
            
            


            


            
