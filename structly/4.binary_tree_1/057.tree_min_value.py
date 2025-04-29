# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque
def tree_min_value(root):
  min1 = float("inf")
  queue = deque([root])
  while queue:
    node = queue.popleft()
    min1 = min(min1, node.val)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return min1