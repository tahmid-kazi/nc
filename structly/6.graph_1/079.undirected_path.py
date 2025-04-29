def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  return dfs(graph, node_A, node_B, set())

def build_graph(edges):
  graph = {}
  for a, b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph

def dfs(graph, src, dst, visited):
  if src == dst:
    return True
  if src in visited:
    return False
  visited.add(src)
  for nei in graph[src]:
    if dfs(graph, nei, dst, visited) == True:
      return True
  return False