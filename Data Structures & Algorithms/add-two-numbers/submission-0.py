# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        while l1:
            str1 = str(l1.val) + str1
            l1 = l1.next
        str2 = ""
        while l2:
            str2 = str(l2.val) + str2
            l2 = l2.next
        num1, num2 = int(str1), int(str2)
        total = num1 + num2
        curr = None
        for num in str(total):
            newNode = ListNode(int(num), curr)
            curr = newNode
        return newNode
