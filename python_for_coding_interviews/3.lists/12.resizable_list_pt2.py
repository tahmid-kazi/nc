from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)
    return arr1
  
# was stumped 250pm
# finally finished (1/8/25)(658-712pm)(Wed)
def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    foo = []
    for a in arr1:
        if a not in arr2:
            foo.append(a)
    return foo


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
