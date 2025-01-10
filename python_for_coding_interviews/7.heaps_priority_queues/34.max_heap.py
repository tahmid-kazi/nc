import heapq
from typing import List

# done (943-949am)(1/10/25)(Fri)
def get_reverse_sorted(nums: List[int]) -> List[int]:
    # go step by step
    max_heap = []
    for i in nums:
        heapq.heappush(max_heap, -i) # first fill the pseudo-max_heap
    
    # then make it a real max_heap
    results = []
    while max_heap:
        results.append(-heapq.heappop(max_heap))
    return results






# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
