def has_subarray_sum(numbers, target_sum):

  # first create a running sum (prefix sum!!!)
  prefix_sums = [0] # this weird trick
  sum = 0
  for num in numbers:
    sum += num
    prefix_sums.append(sum)

  # now do the final step
  seen = set()
  for var in prefix_sums:
      complement = var - target_sum
      if complement in seen:
        return True
      seen.add(var)
  return False