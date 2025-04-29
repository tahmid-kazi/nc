# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  current1, current2 = head_1.next, head_2
  tail = head_1
  count = 0
  while current1 and current2:
    if count % 2 == 0:
      tail.next = current2
      current2 = current2.next
      tail = tail.next
      count += 1
    else:
      tail.next = current1
      current1 = current1.next
      tail = tail.next
      count += 1

  if current1:
    tail.next = current1
  if current2:
    tail.next = current2

  return head_1
