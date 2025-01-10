import heapq
from typing import List

# unit 6 done at 917am
# this = unit 7
# done (1/10/25)(917-920am)(Fri)
def heap_push(heap: List[int], value: int) -> int:
    heapq.heappush(heap, value)
    return heap[0] # min_heap


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
