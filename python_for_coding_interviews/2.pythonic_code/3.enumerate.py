from typing import List

# was stumped (1/8/25)(250 to 302am) and (1/8/25)(1219pm)
# finally got it 1/8/25 - (1253 to 1257pm)(Wed)
def get_index_of_seven(nums: List[int]) -> int:
    for i, name in enumerate(nums):
        if name == 7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    oc = 0
    i1, i2 = 0, 0
    for i, name in enumerate(nums):
        if name == 7:
            oc += 1
            if oc == 2:
                i2 = i
                return i2-i1
            else:
                i1 = i

            


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
