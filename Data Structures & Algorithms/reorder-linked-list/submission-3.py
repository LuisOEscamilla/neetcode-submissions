# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reversing second list
        
        curr = slow.next
        prev = slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        ptr1 = head
        ptr2 = prev
        while ptr2:
            temp1, temp2 = ptr1.next, ptr2.next
            ptr1.next = ptr2
            ptr2.next = temp1 
            ptr1 = temp1
            ptr2 = temp2
    

        