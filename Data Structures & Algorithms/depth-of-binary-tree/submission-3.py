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
            
            if curr:
                maxLayer = max(maxLayer, layer)
                stack.append((curr.left, layer+1))
                stack.append((curr.right, layer+1))
        
        return maxLayer



