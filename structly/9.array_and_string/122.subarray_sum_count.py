from collections import Counter

def subarray_sum_count(numbers, target_sum):

  #first keep a table of prefix sums
  prefix_sums = [0]
  sum = 0
  for num in numbers:
    sum += num
    prefix_sums.append(sum)

  # then use a set to keep track of seen items and use a complement to find the missing match

  seen = Counter()
  counter = 0
  for var in prefix_sums:
    complement = var - target_sum
    counter += seen[complement]
    seen[var] += 1
  return counter