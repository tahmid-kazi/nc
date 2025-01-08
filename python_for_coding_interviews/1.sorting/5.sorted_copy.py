from typing import List

# 1/7/24) 1130-1132pm) Tue night)
def sort_words(words: List[str]) -> List[str]:
    return sorted(words)

def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers, key=abs, reverse=True)


# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))
