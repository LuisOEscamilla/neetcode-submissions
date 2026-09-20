"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        pairs = {None:None}
        dummy = Node(-1)
        prev = dummy
        dummyHead = head
        while dummyHead:
            curr = Node(dummyHead.val)
            prev.next = curr
            pairs[dummyHead] = curr
            prev = curr
            dummyHead = dummyHead.next
        curr = dummy.next
        while head:
            rand = head.random
            curr.random = pairs[rand]
            head = head.next
            curr = curr.next

        return dummy.next
