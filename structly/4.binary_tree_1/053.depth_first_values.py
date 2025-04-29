# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  result = []

  def dfs(root):
    if not root:
      return 
    result.append(root.val)
    dfs(root.left)
    dfs(root.right)
  dfs(root)
  return result
