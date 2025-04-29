# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  list21 = []

  while head:
    list21.append(head.val)
    head = head.next
  return list21
