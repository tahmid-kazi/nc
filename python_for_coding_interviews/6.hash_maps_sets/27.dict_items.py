from typing import Dict, List, Tuple

# done (1/10/25)(847-850am)(Fri)
def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    list1 = []
    for key, val in age_dict.items():
        list1.append((key,val))
    return list1

# do not modify below this line
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}))
print(get_dict_items({'Bob': 30, 'David': 40, 'Charlie': 35, 'Alice': 25, 'Eve': 45}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45, 'Frank': 50}))
