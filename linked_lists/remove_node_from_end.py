"""
1)first, iterate through linked list to count length
2)convert n from end of list to beginning of list
3)iterate through linked list again
    -use transformed n to delete

node to delete:
x - n + 1 <- 1-based indexing

stop 1 node early
    -cur.next = cur.next.next
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        if length == n:
            return head.next
        prev_node = length - n
        dummy = head
        current_position = 0
        while dummy:
            current_position += 1
            if current_position == prev_node:
                dummy.next = dummy.next.next
                break
            dummy = dummy.next
        return head

        