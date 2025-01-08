from typing import List

# was done with Unit 2 - Pythonic Code @ 117pm 1/8/25
# this = (Unit 3)
# this module done 1/8/25 - (130-134pm) - Wed
def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for j in arr2:
        arr1.append(j)
    return arr1


def pop_n(arr: List[int], n: int) -> List[int]:
    if n > len(arr):
        return []
    else:
        for i in range(n):
            arr.pop()
        return arr


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    arr.insert(index, element)
    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
