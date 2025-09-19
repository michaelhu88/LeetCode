class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        cur_node = self.cache[key]

        cur_prev_joint = cur_node.prev
        cur_next_joint = cur_node.next
        cur_prev_joint.next = cur_next_joint
        cur_next_joint.prev = cur_prev_joint

        self.right.prev.next = cur_node
        cur_node.prev = self.right.prev
        cur_node.next = self.right
        self.right.prev = cur_node

        return cur_node.value
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cur_node = self.cache[key]
            cur_prev_joint = cur_node.prev
            cur_next_joint = cur_node.next
            cur_prev_joint.next = cur_next_joint
            cur_next_joint.prev = cur_prev_joint

            self.right.prev.next = cur_node
            cur_node.prev = self.right.prev
            cur_node.next = self.right
            self.right.prev = cur_node
            self.cache[key].value = value
        else:
            new_node = Node(key, value)
            right_prev = self.right.prev
            right_prev.next = new_node
            new_node.prev = right_prev
            new_node.next = self.right
            self.right.prev = new_node

            self.cache[key] = new_node
            if len(self.cache) > self.cap: #time to remove from cache and LRU
                lru_node = self.left.next
                left_next_joint = lru_node.next

                self.left.next = left_next_joint
                left_next_joint.prev = self.left

                del self.cache[lru_node.key]
        return











        
