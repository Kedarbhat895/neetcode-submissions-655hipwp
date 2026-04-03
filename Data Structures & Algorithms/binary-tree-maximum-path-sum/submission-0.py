class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ans = float('-inf')

        def dfs(root):
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            self.ans = max(left + right + root.val, self.ans)
            return root.val + max(left, right)

        dfs(root)
        return self.ans