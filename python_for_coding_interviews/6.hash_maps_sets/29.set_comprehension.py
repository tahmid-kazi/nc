from typing import List, Set

# done (911-912am)(1/10/25)(Fri)
def double_nums(nums: List[int]) -> Set[int]:
    bruh3 = {num*2 for num in nums}
    return bruh3


# do not modify below this line

output1 = double_nums([1, 2, 3])
print(type(output1)) 
print(sorted(list(output1)))

output2 = double_nums([4, -2, 0, 7])
print(type(output2)) 
print(sorted(list(output2)))

output3 = double_nums([10, 20, 30, 40, 50])
print(type(output3)) 
print(sorted(list(output3)))
