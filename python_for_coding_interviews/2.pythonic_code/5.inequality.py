from typing import List

# 1/8/25 - 108 to 112pm - Wed
def is_arr_valid(names: List[str], max_length: int) -> bool:
    return 0 < len(names) <= max_length



# do not modify below this line
print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 1))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 4))
