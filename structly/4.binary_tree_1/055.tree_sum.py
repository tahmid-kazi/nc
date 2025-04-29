# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):

  def dfs(root):
    if not root:
      return 0
    return root.val + dfs(root.left) + dfs(root.right)
  return dfs(root)
  