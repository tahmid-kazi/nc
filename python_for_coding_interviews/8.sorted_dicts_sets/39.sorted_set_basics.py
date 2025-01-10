from typing import List
from sortedcontainers import SortedSet

# this was tricky
# Unit 8 + full course done! (1/10/25) (1037-1044am) (Fri)
def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:

    for i in nums1: 
        sorted_set.add(i)
    for j in nums2:
        if j in sorted_set:
            sorted_set.remove(j)
    return [i for i in sorted_set[0:3]]


# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
