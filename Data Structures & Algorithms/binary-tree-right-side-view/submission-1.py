# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        results = []
        stack = deque()
        layers = set()
        stack.append((root, 1))
        while stack:
            curr, l = stack.popleft()
            if l not in layers:
                results.append(curr.val)
                layers.add(l)
            if curr.right:
                stack.append((curr.right, l+1))
            if curr.left:
                stack.append((curr.left, l+1))
        return results