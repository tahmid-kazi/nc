def pair_product(numbers, target_product):
  hashmap = {}
  for j in range(len(numbers)):
    complement = target_product//numbers[j]
    if complement in hashmap:
      return (hashmap[complement], j)
    hashmap[numbers[j]] = j
    