def intersection(a, b):
  # brute force
  # newlist = []
  # for i in range(len(a)):
  #   for j in range(len(b)):
  #     if a[i] == b[j]:
  #       newlist.append(a[i])
  # return newlist

  # optimal = set()
  newlist = []
  set_a = set(a)
  for i in range(len(b)):
    if b[i] in set_a:
      newlist.append(b[i])
  return newlist