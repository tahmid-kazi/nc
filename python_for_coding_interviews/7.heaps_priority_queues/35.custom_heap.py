import heapq
from typing import List

# done (1/10/25) (Fri) (949-956am)
def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    for i in nums:
        pair = (-i, i)
        heapq.heappush(max_heap, pair) # the heap is a min_heap based on the first element of each tuple

    result = []
    while max_heap:
        pair = heapq.heappop(max_heap)
        result.append(pair[1])
    return result


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
