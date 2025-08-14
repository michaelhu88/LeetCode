from collections import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            one = -heapq.heappop(max_heap)
            two = -heapq.heappop(max_heap)

            remaining = one - two
            if remaining:
                heapq.heappush(max_heap, -remaining)
        
        if not max_heap:
            return 0
        return -max_heap[0]