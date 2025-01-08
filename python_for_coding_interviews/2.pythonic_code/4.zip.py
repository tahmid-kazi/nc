from typing import List, Dict

# 1/8/25 - 1256 to 1259pm) Wed)
def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    dict1 = {}
    for name, score in zip(names, scores):
        dict1[name] = score
    return dict1

# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
