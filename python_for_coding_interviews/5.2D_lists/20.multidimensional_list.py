from typing import List

# 1/8/25 (839-841pm) (Wed)
def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    ret1 = []
    for a in nested_arr:
        ret1.append(max(a))
    return ret1


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
