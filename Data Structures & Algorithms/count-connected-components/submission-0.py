class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphs={i: [] for i in range(n)}
        for a,b in edges:
            graphs[a].append(b)
            graphs[b].append(a)
        
        def dfs(node, path):
            if node in path:
                return  
            path.add(node)
            for nei in graphs[node]:
                dfs(nei, visited)
        visited = set()
        count=0
        for node,_ in graphs.items():
            print(node)
            if node in visited:
                continue
            else: 
                dfs(node, visited)
                count +=1

        return count