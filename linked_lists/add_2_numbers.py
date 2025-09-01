# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1) head = ListNode()
cur = head 
2) initialize carryover = 0
while l1 and l2:
    sum = (l1.val + l2.val + carryover) 
    sum % 10 <-remainder
    sum // 10 <-carryover

    cur.next = ListNode(remainder)
    cur = cur.next

    l1, l2 = l1.next, l2.next

while l1:
    sum = l1.val + carryover
    sum % 10 <-remainder
    sum // 10 <-carryover

    cur.next = ListNode(remainder)
    cur = cur.next

while l2:
    sum = l2.val + carryover
    sum % 10 <-remainder
    sum // 10 <-carryover

    cur.next = ListNode(remainder)
    cur = cur.next

if carryover:
    cur.next = ListNode(1)

return head.next
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        carryover = 0

        while l1 and l2:
            addition = (l1.val + l2.val + carryover) 
            remainder = addition % 10 
            carryover = addition // 10 

            cur.next = ListNode(remainder)
            cur = cur.next

            l1, l2 = l1.next, l2.next

        while l1:
            addition = l1.val + carryover
            remainder = addition % 10 
            carryover = addition // 10 

            cur.next = ListNode(remainder)
            cur = cur.next
            l1 = l1.next

        while l2:
            addition = l2.val + carryover
            remainder = addition % 10 
            carryover = addition // 10 

            cur.next = ListNode(remainder)
            cur = cur.next
            l2 = l2.next

        if carryover:
            cur.next = ListNode(1)

        return head.next




        