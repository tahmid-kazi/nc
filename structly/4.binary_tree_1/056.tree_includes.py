# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):

  def dfs(root, target):
    if not root: return False
    if root.val == target:
      return True
    return dfs(root.left, target) or dfs(root.right, target)
  return dfs(root, target)
    