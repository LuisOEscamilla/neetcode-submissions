# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # if root.left and root.right:
        #     return max(maxDepth(root.right), maxDepth(root.left)) + 1
        # elif root.right:
        #     return 1 + root.right
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1