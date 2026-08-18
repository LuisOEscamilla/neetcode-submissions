# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        pt1 = list1
        pt2 = list2
        if list1.val < list2.val:
            newhead = list1
            pt1 = list1.next
        else:
            newhead = list2
            pt2 = list2.next
        curr = newhead
        while pt2 and pt1:
            if pt1.val < pt2.val:
                curr.next = pt1
                pt1 = pt1.next
            else:
                curr.next = pt2
                pt2 = pt2.next
            curr = curr.next
        if pt1:
            curr.next = pt1
        elif pt2:
            curr.next = pt2

        return newhead