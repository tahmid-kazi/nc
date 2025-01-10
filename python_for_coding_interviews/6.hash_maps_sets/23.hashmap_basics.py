from typing import List, Dict

# 1/9/25 - (723 to 726pm) - Thurs
def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    hashmap = {}
    for key, val in zip(keys, values):
        hashmap[key] = val
    return hashmap

def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    arr = []
    for i in keys:
        arr.append(hash_map[i])
    return arr


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
