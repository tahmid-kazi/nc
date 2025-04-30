def running_sum(numbers):
  sum = 0
  result = []
  for i in range(len(numbers)):
    sum = sum+numbers[i]
    result.append(sum)
  return result 