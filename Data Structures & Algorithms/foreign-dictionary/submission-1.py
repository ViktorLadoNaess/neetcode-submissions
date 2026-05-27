class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Create node for every unique character
        graph = {char: set() for word in words for char in word}

        # 2. Build ordering edges
        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]

            # Invalid prefix case: "abc" before "ab"
            if len(first) > len(second) and first[:len(second)] == second:
                return ""

            for c1, c2 in zip(first, second):
                if c1 != c2:
                    graph[c1].add(c2)
                    break

        # 3. DFS topological sort
        visited = {}  # char -> True if safe, False if currently visiting
        result = []

        def dfs(char):
            if char in visited:
                return visited[char]

            # mark as currently visiting
            visited[char] = False

            for nei in graph[char]:
                if not dfs(nei):
                    return False

            # mark as safe/done
            visited[char] = True
            result.append(char)

            return True

        # 4. Run DFS from every character
        for char in graph:
            if not dfs(char):
                return ""

        # 5. Reverse postorder result
        result.reverse()
        return "".join(result)