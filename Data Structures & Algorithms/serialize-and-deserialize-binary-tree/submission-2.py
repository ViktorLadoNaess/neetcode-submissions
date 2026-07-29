class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(curr):
            if curr is None:
                res.append('null')
                return
            res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        d = data.split(',')
        i = 0

        def dfs():
            nonlocal i
            val = d[i]
            i += 1
            if val == 'null':
                return None
            curr = TreeNode(int(val))
            curr.left = dfs()
            curr.right = dfs()
            return curr

        return dfs()