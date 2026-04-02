# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        def dfs(root, count):
            if not root:
                return count
            
            left = dfs(root.left, count) + 1
            right = dfs(root.right, count)+1

            ans = max(left, right)
            return ans
        
        return dfs(root, 0)

            


            

            
        