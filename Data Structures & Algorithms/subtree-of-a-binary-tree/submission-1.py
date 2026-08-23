# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append(root)  
        matches = deque()
        while stack:
            curr = stack.pop()
            if curr.val == subRoot.val:
                matches.append(curr)
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)

        
        #now that we found matches check if any work
        for match in matches:
            result = self.isSameTree(match, subRoot)
            if result == True:
                return True

        return False

    def isSameTree(self, root, sub):
        if not root and not sub:
            return True
        
        if root and not sub:
            return False
        elif sub and not root:
            return False
        elif sub.val != root.val:
            return False
        else:
            return self.isSameTree(root.left, sub.left) and self.isSameTree(root.right, sub.right)





