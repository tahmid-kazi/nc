from typing import List, Set, Tuple

#this is tricky
# 1/10/25) Fri) 912-917am)
# unit 6 done
def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    bruh4 = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                bruh4.add((i,j))
    return bruh4


# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
