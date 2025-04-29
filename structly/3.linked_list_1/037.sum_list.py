# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  sum21 = 0
  while head:
    sum21 += head.val
    head = head.next
  return sum21
