from typing import List, Tuple

# 1/8/25 - 230am - Tue night
def best_student(scores: List[Tuple[str, int]]) -> str:
    highest = 0
    ret_name = ""
    for x,y in scores:
        if y > highest:
            highest = y
            ret_name = x
        
    return ret_name

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
