# from collections import Counter
# def compress(s):
#   string1 = []
#   table = Counter(s)
#   for char, freq in table.items():
#     if freq == 1:
#       string1.append(str(char))
#     else:
#       string1.append(str(freq)+str(char))
  
#   return "".join(string1)


def compress(s):
  s = s + "@"
  newstr = []
  i, j = 0, 0
  while j < len(s):
    if s[i] == s[j]:
      j+= 1
    else:
      num = j - i
      if num == 1:
        newstr.append(s[i])        
      else:
        newstr.append(str(num)+str(s[i]))  
      i = j
  return "".join(newstr)
    