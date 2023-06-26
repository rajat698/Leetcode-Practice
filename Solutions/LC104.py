class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root):

            if not root:
                return 0
            
            else:
                return 1 + max(dfs(root.left), dfs(root.right))
        
        return dfs(root)