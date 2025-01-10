from typing import List, Dict

# done (1/10/25)(845-847am)(Fri)
def num_to_index(nums: List[int]) -> Dict[int, int]:
    bruh2 = {nums[i]: i for i in range(len(nums))}
    return bruh2

# do not modify below this line
print(num_to_index([1, 2, 3, 4, 5, 6, 7, 8]))
print(num_to_index([8, 7, 6, 5, 4, 3, 2, 1]))
print(num_to_index([0, 3, 2, 4, 5, 1]))
