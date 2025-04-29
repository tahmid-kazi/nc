# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
def breadth_first_values(root):
  if root is None: return []
  result = []
  queue = deque([root])

  while queue:
    node = queue.popleft()
    result.append(node.val)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return result