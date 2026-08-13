class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def height(node):
            nonlocal best
            if node is None:
                return 0
            l = height(node.left)
            r = height(node.right)
            best = max(best, l + r)   # path through this node, in edges
            return 1 + max(l, r)      # height of this subtree
        height(root)
        return best