from typing import List, Deque
from collections import deque

# (1/8/25)(755 to 801pm)(Wed) gpt
def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque(arr)
    for _ in range(k):
        bruh = queue.pop()
        queue.appendleft(bruh)
    return queue

# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
