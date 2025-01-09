from typing import List

# 1/8/25-(719 to 722pm)(Wed)
def create_list_of_odds(n: int) -> List[int]:
    result = [i for i in range(n+1) if i%2 == 1] # 1 to n inclusive
    return result

# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
