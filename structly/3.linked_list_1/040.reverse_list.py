# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
  prev = None
  curr = head
  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  return prev
