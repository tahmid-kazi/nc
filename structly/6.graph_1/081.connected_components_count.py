def connected_components_count(graph):
  visited = set()
  count = 0

  for node in graph:
    if dfs(graph, node, visited) == True:
      count += 1
  return count
  
def dfs(graph, node, visited):
  if node in visited:
    return False 
  visited.add(node)

  for neigbor in graph[node]:
    dfs(graph, neigbor, visited)

  return True
  