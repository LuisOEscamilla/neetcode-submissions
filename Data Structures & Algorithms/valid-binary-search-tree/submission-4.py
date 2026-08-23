# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = deque()
        maximum = float("inf")
        minimum = -float("inf")
        stack.append((root, minimum, maximum))
        while stack:
            curr, minimum, maximum = stack.pop()
            if curr.val >= maximum or curr.val <= minimum:
                return False

            if curr.left and curr.left.val >= curr.val:
                return False
            if curr.right and curr.right.val <= curr.val:
                return False


            if curr.left:
                stack.append((curr.left, minimum, curr.val))
            if curr.right:
                stack.append((curr.right, curr.val, maximum))

        return True
