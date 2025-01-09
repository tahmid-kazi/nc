from typing import List

# (1/8/25)(844 to 847pm)(Wed) 5th Unit done
def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    bruh = [[value for i in range(cols)] for j in range(rows)]
    return bruh



# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
