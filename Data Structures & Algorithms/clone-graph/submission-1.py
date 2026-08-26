"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        stack = deque()
        stack.append(node)
        pair = {}
        while stack:
            curr = stack.pop()
            if curr not in pair:
                copy = Node(curr.val)
                pair[curr] = copy
            for neighbor in curr.neighbors:
                if neighbor not in pair:
                    neighborCopy = Node(neighbor.val)
                    pair[neighbor] = neighborCopy
                    stack.append(neighbor)
                else:
                    neighborCopy = pair[neighbor]
                pair[curr].neighbors.append(pair[neighbor])
                

        return pair[node]
                




        return head