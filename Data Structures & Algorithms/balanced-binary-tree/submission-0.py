# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def dfs(curr):
            nonlocal isBalanced
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            if isBalanced and abs(right-left) > 1:
                isBalanced = False
            
            return 1 + max(left, right)

        dfs(root)
        return isBalanced



