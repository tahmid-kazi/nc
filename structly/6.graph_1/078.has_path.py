def has_path(graph, src, dst):

  if src == dst:
    return True
    
  for neighbors in graph[src]:
    if has_path(graph, neighbors, dst):
      return True
  
  return False