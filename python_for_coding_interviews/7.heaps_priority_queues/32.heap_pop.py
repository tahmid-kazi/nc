import heapq
from typing import List

# done (923-927am) (1/10/25) (Fri)
def heap_pop(heap: List[int]) -> List[int]:
    list4 = []
    while heap:
        list4.append(heapq.heappop(heap))
    return list4

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
