# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        nthNode = length - n

        dummy = ListNode(None, head)
        curr = dummy
        count = 0
        while curr:
            if count == nthNode:
                curr.next = curr.next.next  
            count += 1
            curr = curr.next


        return dummy.next