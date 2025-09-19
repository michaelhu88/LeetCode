"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

1. initialize defaultdict
2. first pass, map cur to new node
3. second pass, connect our new nodes using 
hm[cur.next]
hm[cur.random]
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hm = {None:None}
        cur = head
        while cur:
            hm[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            hm[cur].next = hm[cur.next]
            hm[cur].random = hm[cur.random]
            cur = cur.next
        
        return hm[head]










