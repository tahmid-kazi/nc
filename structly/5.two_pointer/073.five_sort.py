def five_sort(nums):
  i, j = 0, len(nums) - 1

  while i < j:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      temp = nums[j]
      nums[j] = nums[i]
      nums[i] = temp
      i += 1
    else:  
      i += 1
  return nums
      
      