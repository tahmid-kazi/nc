from typing import List

# 1/8/25 - (715 to 716pm) (Wed)
def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    bruh2 = [0] * size
    bruh2[index] = value
    return bruh2



# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
