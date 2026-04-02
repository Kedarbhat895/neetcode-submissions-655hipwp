class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            
     
            temp = root.left
            root.left = root.right
            root.right = temp
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            
        dfs(root)
        return root