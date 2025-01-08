from typing import List

# (1/7/25)(Tue)(658-826pm) did 1st 3 modules of sorting
def sort_words(words: List[str]) -> List[str]:
    words.sort()
    return words
    #return sorted(words)

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    return numbers
    #return sorted(numbers)

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort()
    return numbers
    #return sorted(numbers)



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
