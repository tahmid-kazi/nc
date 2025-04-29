def pair_sum(numbers, target_sum):

  hashmap = {}
  for j in range(len(numbers)):
    # now find the second num
    complement = target_sum - numbers[j]
    if complement in hashmap:
      return (hashmap[complement], j)
    
    # add the first num to hashmap
    hashmap[numbers[j]] = j
    