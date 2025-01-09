from typing import List

# 1/8/25) 716 to 719pm) Wed)
def remove_element(arr: List[int], element: int) -> List[int]:
    list_copy = arr[:] #or arr.copy(), or list(arr)
    list_copy.remove(element)
    return list_copy


# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
