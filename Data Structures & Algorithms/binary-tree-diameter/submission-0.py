# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        def dfs(curr):
            nonlocal maxWidth
            if not curr:
                return 0

            leftWidth = dfs(curr.left)
            rightWidth = dfs(curr.right)
            maxWidth = max(leftWidth+rightWidth, maxWidth)

            return 1 + max(leftWidth, rightWidth)
        dfs(root)

        return maxWidth