from typing import List, Set

# 20 nails (850-908am)
# done (1/10/25) (908-911am) (Fri)
def build_hash_set(keys: List[str]) -> Set[str]:
    hashset = set()
    for i in keys:
        hashset.add(i)
    return hashset

def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    list2 = []
    for i in keys:
        if i in hash_set:
            list2.append(True)
        else:
            list2.append(False)
    return list2

# do not modify below this line

output1 = build_hash_set(["Alice", "Bob", "Charlie"])
print(type(output1))         # check the type of the output
print(sorted(list(output1))) # set order is not guaranteed so we need to sort the list

output2 = build_hash_set(["XY", "XX", "YY", "XY", "YX"]) 
print(type(output2))         # check the type of the output
print(sorted(list(output2))) # set order is not guaranteed so we need to sort the list

print(check_keys({"Alice", "Bob", "Charlie"}, ["Alice", "Bob", "Charlie", "David"]))
print(check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']))
print(check_keys({'a', 'c'}, ['d', 'c']))
