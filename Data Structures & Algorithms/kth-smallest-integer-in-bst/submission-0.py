# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        stack = deque()
        seen = set()
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr not in seen:
                seen.add(curr)
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                if curr.left:
                    stack.append(curr.left)
            elif k == 1:
                return curr.val
            else:
                k -= 1