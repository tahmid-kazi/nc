from collections import Counter
from typing import Counter as CounterType

# 1/10/25 - 845am - Fri
def count_chars(s1: str, s2: str) -> CounterType:
    bruh = Counter(s1)
    bruh.update(s2)
    return bruh
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
