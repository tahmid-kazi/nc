# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):

  def dfs(root):
    if not root:
      return float("-inf")
    if not root.left and not root.right:
      return root.val
    return root.val + max(dfs(root.left), dfs(root.right))
  return dfs(root)
