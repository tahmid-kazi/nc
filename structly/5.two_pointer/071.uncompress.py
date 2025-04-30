def uncompress(s):
  result = []
  numbers = "123456789"
  i, j = 0, 0
  while j < len(s):
    if s[j] in numbers:
      j+=1
    else:
      num = int(s[i:j])
      result.append(s[j] * num)
      j += 1 # move away from the current char and onto the next
      i = j 
  return "".join(result)