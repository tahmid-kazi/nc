from collections import defaultdict
from typing import List, Dict

# 1/9/25 - (735 to 750pm) - Thurs
def count_chars(s: str) -> Dict[str, int]:
    s = list(s)
    hashmap = defaultdict(int)
    for i in s:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    return hashmap


# intelligence is overrated, knowledge is underrated
def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    hashmap = defaultdict(list)
    for i in nums:
        if i[0] in hashmap:
            hashmap[i[0]].extend(i[1:])
        else:
            hashmap[i[0]] = i[1:]
    return hashmap

# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
