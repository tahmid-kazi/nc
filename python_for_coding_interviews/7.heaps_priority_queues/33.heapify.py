import heapq
from typing import List

# done (927-933am)(1/10/25)(Fri)
def heapify_strings(strings: List[str]) -> List[str]:
    heapq.heapify(strings)
    list1 = strings
    return list1


def heapify_integers(integers: List[int]) -> List[int]:
    heapq.heapify(integers)
    list2 = integers
    return list2 # this simply outputs the raw heap representation


def heap_sort(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    list3 = []
    while nums:
        list3.append(heapq.heappop(nums)) # this outputs in sorted order due to minheap property
    return list3


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
