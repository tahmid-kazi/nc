from typing import List

# 1/7/25) 1126 to 1130pm) Tue)
def sort_words(words: List[str]) -> List[str]:
    words.sort(key=lambda words: len(words), reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=lambda num: abs(num))
    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
