from typing import List

# 1/8/25 - Wed - (722-728pm)
def reverse_list(arr: List[int]) -> List[int]:
    stack = []
    for a in range(len(arr)-1, -1, -1):
        stack.append(arr[a])
    return stack

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
