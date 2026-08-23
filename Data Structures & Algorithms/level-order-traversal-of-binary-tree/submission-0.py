# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = []
        
        def helper(stack):
            layer = []
            newStack = deque()
            for node in stack:
                layer.append(node.val)
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)

            results.append(layer)
            if newStack:
                helper(newStack)
            return
        helper([root])
        return results