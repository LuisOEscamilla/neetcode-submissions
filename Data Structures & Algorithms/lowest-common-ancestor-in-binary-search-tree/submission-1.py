# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p , q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


    #     stack = deque()
    #     stack.append(root)
    #     LCA = root
    #     while stack:
    #         curr = stack.pop()
    #         if self.containsPQ(curr, p, q):
    #             LCA = curr
    #             if curr.left:
    #                 stack.append(curr.left)
    #             if curr.right:
    #                 stack.append(curr.right)


    #     return LCA

    # def containsPQ(self, root, p, q):
    #     has = 0
    #     stack = deque()
    #     stack.append(root)
    #     while stack:
    #         curr = stack.pop()
    #         if curr == p or curr == q:
    #             has += 1
    #         if curr.left:
    #             stack.append(curr.left)
    #         if curr.right:
    #             stack.append(curr.right)
    #     if has == 2:
    #         return True
    #     else:
    #         return False