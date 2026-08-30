# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        seen = set()
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr == None:
                continue
            if curr not in seen:
                seen.add(curr)
                stack.append(curr.right)
                stack.append(curr)
                stack.append(curr.left)
            elif k == 1:
                return curr.val
            else:
                k -= 1