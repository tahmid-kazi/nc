def sum_numbers_recursive(numbers):
  def recur(numbers):  
    if numbers == []:
      return 0
    return numbers[0] + recur(numbers[1:])
  
  return recur(numbers)