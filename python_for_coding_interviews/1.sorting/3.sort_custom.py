from typing import List

# (1/7/25)(Tue)(658-826pm) did 1st 3 modules of sorting
def get_word_length(arr: List[str]) -> int:
    return len(arr)

def sort_words(words: List[str]) -> List[str]:
    words.sort(reverse=True,key=get_word_length)
    return words

def sort_abs(num: int) -> int:
    if num < 0:
        return -num
    else:
        return num

def sort_numbers(numbers: List[int]) -> List[int]:
    #numbers.sort(key=abs)
    numbers.sort(key=sort_abs)
    return numbers
    # (1/7/25) stumped (742pm), got it (816-826pm)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
