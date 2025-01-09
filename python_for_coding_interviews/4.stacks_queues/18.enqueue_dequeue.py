from typing import List, Deque
from collections import deque

# 1/8/25 (750 to 754pm) (Wed)
def rotate_list(arr: List[int], k: int) -> Deque[int]:
    bruh = deque()
    for a in range(k, len(arr)):
        bruh.append(arr[a])
    for j in range(0,k):
        bruh.append(arr[j])
    return bruh



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
