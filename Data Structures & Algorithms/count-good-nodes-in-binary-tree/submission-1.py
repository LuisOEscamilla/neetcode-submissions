# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return count
        stack = []
        stack.append((root, -101))
        while stack:
            curr, maxSoFar = stack.pop()
            if curr.val >= maxSoFar:
                print(curr.val)
                count += 1
                maxSoFar = curr.val
            if curr.right:
                stack.append((curr.right, maxSoFar))
            if curr.left:
                stack.append((curr.left, maxSoFar))
        return count