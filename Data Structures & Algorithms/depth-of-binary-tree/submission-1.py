# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        # return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
        stack = deque()
        stack.append((root, 1))
        maxLayer = 0
        while stack:
            curr, layer = stack.pop()
            maxLayer = max(maxLayer, layer)
            if curr.left:
                stack.append((curr.left, layer+1))
            if curr.right:
                stack.append((curr.right, layer+1))
        
        return maxLayer



