# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):

  counter1 = 0
  while head:
    if counter1 == index:
      return head.val
    head = head.next
    counter1 += 1
    